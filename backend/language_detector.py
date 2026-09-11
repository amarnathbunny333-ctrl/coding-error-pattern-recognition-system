def detect_language(code):

    code = code.strip()

    if "public class" in code:
        return "java"

    elif "#include" in code:
        return "cpp"

    elif "console.log" in code:
        return "javascript"

    else:
        return "python"