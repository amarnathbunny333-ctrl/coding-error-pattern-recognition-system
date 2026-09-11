import subprocess
import uuid
import os


# ---------------- PYTHON ----------------
def run_python(code):
    try:
        exec(code)
        return "No Errors Found"
    except Exception as e:
        return str(e)


# ---------------- C++ ----------------
def run_cpp(code):

    file_id = str(uuid.uuid4())
    cpp_file = f"{file_id}.cpp"
    exe_file = f"{file_id}.exe"

    with open(cpp_file, "w") as f:
        f.write(code)

    compile_process = subprocess.run(
        ["g++", cpp_file, "-o", exe_file],
        capture_output=True,
        text=True
    )

    if compile_process.returncode != 0:
        return compile_process.stderr

    run_process = subprocess.run(
        [exe_file],
        capture_output=True,
        text=True
    )

    return run_process.stdout or run_process.stderr


# ---------------- JAVA ----------------
def run_java(code):

    file_name = "Main.java"

    with open(file_name, "w") as f:
        f.write(code)

    compile_process = subprocess.run(
        ["javac", file_name],
        capture_output=True,
        text=True
    )

    if compile_process.returncode != 0:
        return compile_process.stderr

    run_process = subprocess.run(
        ["java", "Main"],
        capture_output=True,
        text=True
    )

    return run_process.stdout or run_process.stderr


# ---------------- JAVASCRIPT ----------------
def run_js(code):

    file_name = "temp.js"

    with open(file_name, "w") as f:
        f.write(code)

    process = subprocess.run(
        ["node", file_name],
        capture_output=True,
        text=True
    )

    return process.stdout or process.stderr