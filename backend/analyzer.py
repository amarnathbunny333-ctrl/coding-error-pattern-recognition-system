from backend.language_detector import detect_language
from backend.compiler_engine import (
    run_python,
    run_cpp,
    run_java,
    run_js
)
from backend.error_parser import parse_error
from backend.error_patterns import ERROR_PATTERNS


def analyze_code(code):

    language = detect_language(code)

    print("Detected Language:", language)

    # run code based on language
    if language == "python":
        output = run_python(code)

    elif language == "cpp":
        output = run_cpp(code)

    elif language == "java":
        output = run_java(code)

    elif language == "js":
        output = run_js(code)

    else:
        output = "Unsupported language"

    # parse error
    parsed = parse_error(language, output)

    # suggestion
    suggestion = ERROR_PATTERNS.get(parsed["error_type"], "No suggestion available")

    final_result = {
        "language": language,
        "error_type": parsed["error_type"],
        "message": parsed["message"],
        "line": parsed["line"],
        "suggestion": suggestion
    }

    print("\n=== ANALYSIS RESULT ===")
    print(final_result)

    return final_result

if __name__ == "__main__":

    test_code = """
    #include<iostream> using namespace std;

    int main(){ cout << x;} #change this for testing
      """
    
    analyze_code(test_code)