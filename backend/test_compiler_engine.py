from backend.language_detector import detect_language
from backend.compiler_engine import (
    run_python,
    run_cpp,
    run_java,
    run_javascript
)

print("=" * 50)
print("CODING ERROR PATTERN RECOGNITION SYSTEM")
print("=" * 50)

# Test Code
test_code = """
print("Hello World")
"""

# Detect Language
language = detect_language(test_code)

print("\nDetected Language :", language)

# Execute Code
if language == "python":
    result = run_python(test_code)

elif language == "cpp":
    result = run_cpp(test_code)

elif language == "java":
    result = run_java(test_code)

elif language == "javascript":
    result = run_javascript(test_code)

else:
    result = {
        "success": False,
        "output": "Unsupported Language"
    }

# Display Result
print("\nExecution Status :", result["success"])

print("\nOutput:")
print("-" * 40)
print(result["output"])
print("-" * 40)