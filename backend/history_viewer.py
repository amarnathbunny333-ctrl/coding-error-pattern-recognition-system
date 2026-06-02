def show_history():

    try:

        with open("reports/error_report.txt", "r") as file:
            data = file.read()

        count = data.count("Analysis Result")

        print("\nERROR HISTORY")
        print("=" * 50)

        print("Total Reports:", count)
        print()

        print(data)

    except FileNotFoundError:

        print("No report history found.")


show_history()