ERROR_PATTERNS = {

    "SyntaxError":
        "Check for missing colons (:), brackets, or quotes.",

    "NameError":
        "A variable is being used before it is defined.",

    "ZeroDivisionError":
        "You cannot divide a number by zero.",

    "TypeError":
        "An operation was performed on incompatible data types.",

    "IndexError":
        "The list index is outside the valid range."
}
print(ERROR_PATTERNS["NameError"])