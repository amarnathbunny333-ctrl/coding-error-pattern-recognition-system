def run_code(language, code):

    if language == "python":
        try:
            exec(code)
            return "No Errors Found"
        except Exception as e:
            return f"{type(e).__name__}: {e}"

    elif language == "java":
        return "Java execution simulated (needs compiler integration)"

    elif language == "cpp":
        return "C++ execution simulated (needs g++)"

    elif language == "javascript":
        return "JS execution simulated (needs Node.js)"

    else:
        return "Unsupported Language"