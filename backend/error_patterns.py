ERROR_PATTERNS = {
    "SyntaxError": {
        "meaning": "Your code has incorrect syntax.",
        "suggestion": "Check missing symbols like :, (), {}, or indentation."
    },

    "NameError": {
        "meaning": "You used a variable before defining it.",
        "suggestion": "Define the variable before using it."
    },

    "TypeError": {
        "meaning": "You are using incompatible data types.",
        "suggestion": "Check variable types before operations."
    },

    "ZeroDivisionError": {
        "meaning": "You tried to divide a number by zero.",
        "suggestion": "Avoid dividing by zero."
    },

    "IndentationError": {
        "meaning": "Your code indentation is incorrect.",
        "suggestion": "Fix indentation (use proper spaces)."
    },

    "ReferenceError": {
        "meaning": "Variable is not declared (common in JS).",
        "suggestion": "Declare the variable before use."
    }
}