def generate_statistics():

    with open("reports/error_report.txt", "r") as file:
        data = file.read()

    # ---------------- ERROR COUNTS ----------------
    syntax_count = data.count("SyntaxError")
    name_count = data.count("NameError")
    zero_count = data.count("ZeroDivisionError")
    type_count = data.count("TypeError")
    index_count = data.count("IndexError")
    value_count = data.count("ValueError")
    attribute_count = data.count("AttributeError")
    key_count = data.count("KeyError")

    # ---------------- TOTAL ERRORS ----------------
    total_errors = (
        syntax_count +
        name_count +
        zero_count +
        type_count +
        index_count +
        value_count +
        attribute_count +
        key_count
    )

    # ---------------- DICTIONARY ----------------
    error_counts = {
        "SyntaxError": syntax_count,
        "NameError": name_count,
        "ZeroDivisionError": zero_count,
        "TypeError": type_count,
        "IndexError": index_count,
        "ValueError": value_count,
        "AttributeError": attribute_count,
        "KeyError": key_count
    }

    # ---------------- MOST & LEAST COMMON ----------------
    most_common_error = max(error_counts, key=error_counts.get)
    most_common_count = error_counts[most_common_error]

    least_common_error = min(error_counts, key=error_counts.get)
    least_common_count = error_counts[least_common_error]

    # ---------------- DASHBOARD ----------------
    print("\n" + "=" * 45)
    print("        ERROR STATISTICS DASHBOARD")
    print("=" * 45)

    print(f"SyntaxError       : {syntax_count}")
    print(f"NameError         : {name_count}")
    print(f"ZeroDivisionError : {zero_count}")
    print(f"TypeError         : {type_count}")
    print(f"IndexError        : {index_count}")
    print(f"ValueError        : {value_count}")
    print(f"AttributeError    : {attribute_count}")
    print(f"KeyError          : {key_count}")

    print("-" * 45)
    print(f"Total Errors      : {total_errors}")
    print("-" * 45)

    print(f"Most Common Error : {most_common_error} ({most_common_count})")
    print(f"Least Common Error: {least_common_error} ({least_common_count})")

    print("=" * 45)

    # ---------------- PERCENTAGE DISTRIBUTION ----------------
    if total_errors > 0:
        print("\nError Percentage Distribution:")
        print("-" * 45)

        print(f"SyntaxError       : {syntax_count / total_errors * 100:.2f}%")
        print(f"NameError         : {name_count / total_errors * 100:.2f}%")
        print(f"ZeroDivisionError : {zero_count / total_errors * 100:.2f}%")
        print(f"TypeError         : {type_count / total_errors * 100:.2f}%")
        print(f"IndexError        : {index_count / total_errors * 100:.2f}%")
        print(f"ValueError        : {value_count / total_errors * 100:.2f}%")
        print(f"AttributeError    : {attribute_count / total_errors * 100:.2f}%")
        print(f"KeyError          : {key_count / total_errors * 100:.2f}%")

    print("=" * 45)

    # ---------------- SMART INSIGHTS ----------------
    print("\nSMART INSIGHTS")
    print("=" * 45)

    if most_common_error == "SyntaxError":
        print("Insight: You are making syntax mistakes.")
        print("Fix: Focus on colons, brackets, and indentation.")

    elif most_common_error == "NameError":
        print("Insight: You are using undefined variables.")
        print("Fix: Define variables before using them.")

    elif most_common_error == "ZeroDivisionError":
        print("Insight: You are dividing numbers incorrectly.")
        print("Fix: Avoid dividing by zero.")

    elif most_common_error == "TypeError":
        print("Insight: You are mixing incompatible data types.")
        print("Fix: Check string/int operations.")

    elif most_common_error == "IndexError":
        print("Insight: You are accessing invalid list indexes.")
        print("Fix: Check list boundaries.")

    elif most_common_error == "KeyError":
        print("Insight: You are using missing dictionary keys.")
        print("Fix: Validate keys before accessing.")

    else:
        print("Insight: Your code is stable.")

    # ---------------- FINAL SUMMARY ----------------
    print("\nFINAL SUMMARY")
    print("=" * 45)

    print(f"Total Errors Analyzed : {total_errors}")
    print(f"Most Frequent Issue   : {most_common_error}")
    print(f"Code Health Status    : {'Needs Improvement' if total_errors > 0 else 'Good'}")

    print("=" * 45)


generate_statistics()