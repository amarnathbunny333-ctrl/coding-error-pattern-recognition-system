from error_patterns import ERROR_PATTERNS


def save_report(text):

    with open("reports/error_report.txt", "a") as file:
        file.write(text)
        file.write("\n" + "=" * 50 + "\n")


def analyze_code(code):

    try:
        exec(code)

        result = f"""
Analysis Result
----------------
Code       : {code}
Status     : No Errors Found
"""

        print(result)
        save_report(result)

    except Exception as e:

        error_type = type(e).__name__

        result = f"""
Analysis Result
----------------
Code       : {code}

Error Type : {error_type}
Message    : {e}
Suggestion : {ERROR_PATTERNS.get(error_type, "No suggestion available")}
"""

        print(result)
        save_report(result)


# ---------------- USER INPUT MODE ----------------
print("\nCODING ERROR PATTERN SYSTEM")
print("=" * 40)

while True:

    user_code = input("\nEnter Python code to analyze (or type 'exit' to stop):\n")

    if user_code.lower() == "exit":
        print("Exiting system... Goodbye!")
        break

    analyze_code(user_code)