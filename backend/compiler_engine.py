import subprocess
import tempfile
import os
import sys
import shutil
import traceback
try:
    import resource
except ImportError:
    resource = None
import re


TIMEOUT_SECONDS = 5
MEM_LIMIT_MB = 256


def _limit_resources(cap_address_space=True):
    """Applied in the child process (POSIX only) to cap memory and prevent
    runaway resource usage. Called via preexec_fn.

    cap_address_space=False skips RLIMIT_AS: V8/Node reserves a large
    virtual address space up front regardless of actual memory used, so an
    RLIMIT_AS cap makes it crash immediately.
    """
    if cap_address_space:
        mem_bytes = MEM_LIMIT_MB * 1024 * 1024
        try:
            resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
        except (ValueError, resource.error):
            pass
    try:
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        resource.setrlimit(resource.RLIMIT_NPROC, (64, 64))
    except (ValueError, resource.error):
        pass


def _run_subprocess(cmd, cwd=None, timeout=TIMEOUT_SECONDS, cap_address_space=True):
    """Run a subprocess with timeout, resource limits, and partial-output
    capture even when the process times out."""
    preexec = (lambda: _limit_resources(cap_address_space)) if os.name == "posix" else None
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            preexec_fn=preexec,
        )
        return {
            "success": result.returncode == 0,
            "output": result.stdout if result.returncode == 0 else (result.stderr or result.stdout),
        }
    except subprocess.TimeoutExpired as e:
        partial = ""
        if e.stdout:
            partial += e.stdout if isinstance(e.stdout, str) else e.stdout.decode(errors="replace")
        if e.stderr:
            partial += e.stderr if isinstance(e.stderr, str) else e.stderr.decode(errors="replace")
        msg = f"Execution stopped: Time limit exceeded ({timeout} seconds)"
        if partial.strip():
            msg += f"\n\n--- Partial output before timeout ---\n{partial}"
        return {"success": False, "output": msg}
    except FileNotFoundError as e:
        return {"success": False, "output": f"Required tool not found: {e}"}


# =========================
# PYTHON RUNNER
# =========================

def run_python(code):
    file_path = None
    try:
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".py", mode="w", encoding="utf-8"
        ) as file:
            file.write(code)
            file_path = file.name

        # Prefer the interpreter currently running us; fall back to python3/python
        python_bin = sys.executable or shutil.which("python3") or shutil.which("python")
        if not python_bin:
            return {"success": False, "output": "No Python interpreter found on PATH."}

        return _run_subprocess([python_bin, file_path])

    except Exception:
        return {"success": False, "output": traceback.format_exc()}

    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)


# =========================
# C++ RUNNER
# =========================

def run_cpp(code):
    compiler = shutil.which("g++") or shutil.which("clang++")
    if not compiler:
        return {"success": False, "output": "C++ compiler not found (looked for g++/clang++)."}

    tmpdir = tempfile.mkdtemp()
    try:
        src_path = os.path.join(tmpdir, "main.cpp")
        binary_path = os.path.join(tmpdir, "main.out")

        with open(src_path, "w", encoding="utf-8") as f:
            f.write(code)

        compile_result = subprocess.run(
            [compiler, src_path, "-O2", "-std=c++17", "-o", binary_path],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
        if compile_result.returncode != 0:
            return {"success": False, "output": compile_result.stderr}

        return _run_subprocess([binary_path], cwd=tmpdir)

    except subprocess.TimeoutExpired:
        return {"success": False, "output": "Compilation timed out."}
    except Exception:
        return {"success": False, "output": traceback.format_exc()}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


# =========================
# JAVA RUNNER
# =========================

def run_java(code):
    javac = shutil.which("javac")
    java = shutil.which("java")
    if not javac or not java:
        return {"success": False, "output": "Java JDK not found (looked for javac/java)."}

    tmpdir = tempfile.mkdtemp()
    try:
        # javac requires the file name to match the public class name.
        match = re.search(r"public\s+class\s+(\w+)", code)
        class_name = match.group(1) if match else "Main"

        # If there's no public class, wrap or just name the file after any class,
        # falling back to Main if none is found at all.
        if not match:
            any_class = re.search(r"class\s+(\w+)", code)
            class_name = any_class.group(1) if any_class else "Main"

        src_path = os.path.join(tmpdir, f"{class_name}.java")
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(code)

        compile_result = subprocess.run(
            [javac, src_path],
            cwd=tmpdir,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
        if compile_result.returncode != 0:
            return {"success": False, "output": compile_result.stderr}

        return _run_subprocess([java, "-cp", tmpdir, class_name], cwd=tmpdir)

    except subprocess.TimeoutExpired:
        return {"success": False, "output": "Compilation timed out."}
    except Exception:
        return {"success": False, "output": traceback.format_exc()}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


# =========================
# JAVASCRIPT RUNNER
# =========================

def run_javascript(code):
    node = shutil.which("node")
    if not node:
        return {"success": False, "output": "JavaScript runtime not found (looked for node)."}

    file_path = None
    try:
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".js", mode="w", encoding="utf-8"
        ) as file:
            file.write(code)
            file_path = file.name

        return _run_subprocess(
            [node, f"--max-old-space-size={MEM_LIMIT_MB}", file_path],
            cap_address_space=False,
        )

    except Exception:
        return {"success": False, "output": traceback.format_exc()}

    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)


# =========================
# DISPATCH
# =========================

RUNNERS = {
    "python": run_python,
    "cpp": run_cpp,
    "java": run_java,
    "javascript": run_javascript,
}


def run_code(language, code):
    runner = RUNNERS.get(language)
    if not runner:
        return {"success": False, "output": f"Unsupported language: {language}"}
    return runner(code)


if __name__ == "__main__":
    # Quick smoke test
    print(run_python("print('hello from python')"))