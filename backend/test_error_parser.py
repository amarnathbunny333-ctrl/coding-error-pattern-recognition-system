import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.language_detector import detect_language
from backend.compiler_engine import (
    run_python,
    run_cpp,
    run_java,
    run_javascript
)
from backend.error_parser import parse_error
from backend.statistics import save_error, get_statistics


print("=" * 50)
print("CODING ERROR PATTERN RECOGNITION SYSTEM")
print("=" * 50)


# -----------------------------
# TEST CODE (CHANGE ONLY THIS)
# -----------------------------
test_code = """
for i in range(5)
    print(i)
"""
# -----------------------------


# Step 1: Detect Language
language = detect_language(test_code)
print("\nDetected Language :", language)


# Step 2: Run Code Based on Language
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


# Step 3: Show Raw Output
print("\nRaw Output:")
print("-" * 40)
print(result["output"])
print("-" * 40)


# Step 4: Parse Error (if any)
if not result["success"]:

    parsed = parse_error(language, result["output"])

    print("\n=== ERROR ANALYSIS ===")
    print("Language   :", parsed["language"])
    print("Type       :", parsed["error_type"])
    print("Line       :", parsed["line_number"])
    print("Message    :", parsed["message"])
    print("Meaning    :", parsed["meaning"])
    print("Suggestion :", parsed["suggestion"])
    print("Quick Fix  :", parsed["quick_fix"])

    # Step 5: Save to Statistics DB
    save_error(parsed)


# Step 6: Show Statistics
print("\n=== ERROR STATISTICS ===")
stats = get_statistics()

print("Total Errors   :", stats["total_errors"])
print("Most Common    :", stats["most_common"])
print("Least Common   :", stats["least_common"])