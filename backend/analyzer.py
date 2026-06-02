def analyze_code(code):

    try:
        exec(code)
        print("No Errors Found")

    except Exception as e:
        print("Error Type:", type(e).__name__)
        print("Message:", e)


analyze_code("for i in range(5)")