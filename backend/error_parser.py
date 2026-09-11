import re

def resolve_error(code, language, error_type, message, line_no, col_no):
    if not code or not line_no:
        return None
        
    lines = code.splitlines()
    if not (1 <= line_no <= len(lines)):
        return None
        
    target_line = lines[line_no - 1]
    message_lower = (message or "").lower()
    
    # 1. Python Resolvers
    if language == "python":
        if error_type == "SyntaxError":
            # Missing colon
            trimmed = target_line.rstrip()
            keywords = ["if ", "elif ", "else", "for ", "while ", "def ", "class ", "try", "except"]
            if any(trimmed.startswith(kw) or f" {kw}" in trimmed for kw in keywords) and not trimmed.endswith(":"):
                lines[line_no - 1] = target_line + ":"
                return "\n".join(lines)
                
            # Unterminated string
            if "unterminated string literal" in message_lower or "unterminated triple-quoted string" in message_lower:
                if '"' in target_line and target_line.count('"') % 2 != 0:
                    lines[line_no - 1] = target_line + '"'
                elif "'" in target_line and target_line.count("'") % 2 != 0:
                    lines[line_no - 1] = target_line + "'"
                return "\n".join(lines)
                
            # Unclosed parentheses / brackets
            if "was never closed" in message_lower or "expected ')'" in message_lower or "expected ']'" in message_lower or "expected '}'" in message_lower:
                if "(" in target_line and target_line.count("(") > target_line.count(")"):
                    lines[line_no - 1] = target_line + ")"
                elif "[" in target_line and target_line.count("[") > target_line.count("]"):
                    lines[line_no - 1] = target_line + "]"
                elif "{" in target_line and target_line.count("{") > target_line.count("}"):
                    lines[line_no - 1] = target_line + "}"
                return "\n".join(lines)
                
        elif error_type == "IndentationError":
            # Indentation fix
            if line_no > 1:
                prev_line = lines[line_no - 2]
                prev_indent = len(prev_line) - len(prev_line.lstrip())
                if prev_line.rstrip().endswith(":"):
                    prev_indent += 4
                lines[line_no - 1] = " " * prev_indent + target_line.lstrip()
            else:
                lines[line_no - 1] = "    " + target_line.lstrip()
            return "\n".join(lines)

    # 2. C++ & Java Resolvers
    elif language in ["cpp", "java"]:
        if "expected ';'" in message_lower or "';' expected" in message_lower or ("expected" in message_lower and ";" in message_lower):
            lines[line_no - 1] = target_line.rstrip() + ";"
            return "\n".join(lines)
            
        elif "not declared" in message_lower or "cannot find symbol" in message_lower:
            symbol_match = re.search(r"'([^']+)'", message or "")
            if not symbol_match:
                symbol_match = re.search(r"symbol:\s+variable\s+(\w+)", message or "")
            if symbol_match:
                symbol = symbol_match.group(1)
                indent_len = len(target_line) - len(target_line.lstrip())
                indent = " " * indent_len
                decl = f"{indent}int {symbol} = 0; // Declared automatically"
                lines.insert(line_no - 1, decl)
                return "\n".join(lines)

    # 3. JavaScript Resolvers
    elif language == "javascript":
        if "unexpected token ';'" in message_lower or "unexpected token" in message_lower:
            if "(" in target_line and target_line.count("(") > target_line.count(")"):
                if target_line.rstrip().endswith(";"):
                    lines[line_no - 1] = target_line.rstrip()[:-1] + ");"
                    return "\n".join(lines)
                    
        elif "is not defined" in message_lower:
            symbol_match = re.search(r"(\w+)\s+is not defined", message or "")
            if symbol_match:
                symbol = symbol_match.group(1)
                indent_len = len(target_line) - len(target_line.lstrip())
                indent = " " * indent_len
                decl = f"{indent}let {symbol} = 0; // Declared automatically"
                lines.insert(line_no - 1, decl)
                return "\n".join(lines)

    return None


def explain_error(language, error_type, message):
    msg_lower = (message or "").lower()
    
    # Defaults
    meaning = "An execution error occurred."
    suggestion = "Check code syntax and logic around the reported line."
    
    if language == "python":
        if error_type == "SyntaxError":
            if "unterminated string literal" in msg_lower or "unterminated triple-quoted string" in msg_lower:
                meaning = "Your code contains a string literal that was opened but never closed."
                suggestion = "Add a closing quotation mark matching the opening quotation mark (single or double quote)."
            elif "expected ':'" in msg_lower:
                meaning = "A colon (:) is missing at the end of a block statement (e.g. if, for, while, def, class)."
                suggestion = "Append a colon ':' at the end of the block declaration line."
            elif "was never closed" in msg_lower:
                bracket_type = "parenthesis/bracket"
                if "{" in msg_lower: bracket_type = "curly brace '{'"
                elif "[" in msg_lower: bracket_type = "square bracket '['"
                elif "(" in msg_lower: bracket_type = "parenthesis '('"
                meaning = f"An opened {bracket_type} was never closed."
                suggestion = f"Locate the unclosed {bracket_type} and add a matching closing symbol."
            else:
                meaning = "Your Python code contains incorrect syntax."
                suggestion = "Verify all parentheses, brackets, quotes, and colons are correct."
        elif error_type == "NameError":
            var_name = "variable/function"
            symbol_match = re.search(r"'([^']+)'", message or "")
            if symbol_match:
                var_name = f"'{symbol_match.group(1)}'"
            meaning = f"The name {var_name} is used but has not been defined in the current scope."
            suggestion = f"Define {var_name} by assigning a value to it, or check for spelling typos."
        elif error_type == "TypeError":
            meaning = "An operation or function was applied to an object of incompatible type."
            suggestion = "Verify the types of variables involved (e.g. do not add strings to integers without conversion)."
        elif error_type == "ZeroDivisionError":
            meaning = "A division or modulo operation was attempted with a denominator of zero."
            suggestion = "Check your variables and add a safety check (e.g., if denominator != 0) before dividing."
        elif error_type == "IndentationError":
            meaning = "The indentation of your code blocks is inconsistent or invalid."
            suggestion = "Check your indentation. Python requires consistent use of spaces (standard is 4) or tabs within nested blocks."
        elif error_type == "IndexError":
            meaning = "You tried to access a list or sequence index that is out of range."
            suggestion = "Verify the length of the list and ensure your index is between 0 and len(list) - 1."
        elif error_type == "KeyError":
            meaning = "You tried to access a dictionary key that does not exist."
            suggestion = "Check that the key exists in the dictionary, or use the .get() method to provide a default value."
            
    elif language == "cpp":
        if "expected ';'" in msg_lower or "expected" in msg_lower and ";" in msg_lower:
            meaning = "A statement is missing a semicolon (;) at the end."
            suggestion = "Add a semicolon ';' to terminate the statement on the indicated line."
        elif "expected" in msg_lower and ("}" in msg_lower or "]" in msg_lower or ")" in msg_lower):
            meaning = "An opening parenthesis, bracket, or curly brace is not closed."
            suggestion = "Add the matching closing brace/bracket to balance the block structure."
        elif "not declared" in msg_lower or "undeclared" in msg_lower:
            var_name = "variable"
            symbol_match = re.search(r"'([^']+)'", message or "")
            if symbol_match:
                var_name = f"'{symbol_match.group(1)}'"
            meaning = f"The {var_name} is used but has not been declared or is out of scope."
            suggestion = f"Declare the variable {var_name} with a valid type (e.g. int, float, string) before using it."
        elif "expected constructor, destructor, or type conversion" in msg_lower:
            meaning = "Syntax error in top-level declarations or class definition."
            suggestion = "Check that class definitions end with a semicolon (};) and check global function declarations."
            
    elif language == "java":
        if "';' expected" in msg_lower:
            meaning = "A statement is missing a semicolon (;) at the end."
            suggestion = "Add a semicolon ';' at the end of the statement."
        elif "cannot find symbol" in msg_lower:
            symbol_name = "variable/class/method"
            symbol_match = re.search(r"symbol:\s+variable\s+(\w+)", message or "")
            if symbol_match:
                symbol_name = f"'{symbol_match.group(1)}'"
            meaning = f"The compiler cannot find the {symbol_name} declaration."
            suggestion = f"Verify that {symbol_name} is spelled correctly, declared in this scope, or import the necessary class."
        elif "missing return statement" in msg_lower:
            meaning = "A non-void method is missing a return statement in some execution paths."
            suggestion = "Add a return statement that returns a value of the correct type at the end of the method."
        elif "reached end of file while parsing" in msg_lower:
            meaning = "The file ended without closing all opened curly braces '{' or brackets."
            suggestion = "Count open/close braces and ensure they are all closed."
            
    elif language == "javascript":
        if "unexpected token ';'" in msg_lower or "unexpected token" in msg_lower:
            meaning = "The JavaScript runtime found unexpected tokens while parsing."
            suggestion = "Check for missing commas, brackets, or misplaced operators near the error column."
        elif "is not defined" in msg_lower:
            meaning = "You accessed a variable that does not exist or has not been declared."
            suggestion = "Declare the variable using let, const, or var, or check for typos."
        elif "is not a function" in msg_lower:
            meaning = "You tried to invoke something that is not callable."
            suggestion = "Make sure the variable holds a function before invoking it."
            
    return meaning, suggestion


def extract_line_and_column(language, error_output):
    line_no = None
    col_no = None
    
    # 1. Match standard file:line:col pattern (e.g. file.cpp:5:12, file.js:2:13)
    match_file_line_col = re.search(r'\.(?:py|cpp|java|js|out):(\d+):(\d+)', error_output)
    if match_file_line_col:
        line_no = int(match_file_line_col.group(1))
        col_no = int(match_file_line_col.group(2))
    else:
        # 2. Match file:line pattern (e.g. file.py:5, file.java:5) or "line X" (Python)
        match_file_line = re.search(r'(?:\.(?:py|cpp|java|js):|line\s+)(\d+)', error_output)
        if match_file_line:
            line_no = int(match_file_line.group(1))
            
    # 3. If line found but column not yet found, look for caret '^' line
    if line_no and not col_no:
        lines = error_output.splitlines()
        for line in lines:
            stripped = line.strip()
            if stripped and all(c in " ^~-" for c in line) and "^" in line:
                col_no = line.find("^") + 1
                break
                
    return line_no, col_no


def extract_error_details(language, error_output):
    error_type = "Error"
    message = error_output.strip().splitlines()[-1] if error_output.strip() else "Unknown execution error"
    
    # 1. Look for Python/JS pattern: NameError: name 'x' is not defined
    match_py_js = re.search(r'([A-Za-z]+(?:Error|Exception)):\s*(.*)', error_output)
    if match_py_js:
        error_type = match_py_js.group(1)
        message = match_py_js.group(2)
    else:
        # 2. Look for compiler error pattern: error: expected ';' before '}'
        match_compiler = re.search(r'error:\s*(.*)', error_output, re.IGNORECASE)
        if match_compiler:
            error_type = "Compile Error"
            message = match_compiler.group(1)
            
            # Refine error type
            if "expected" in message.lower() or "missing" in message.lower():
                error_type = "SyntaxError"
            elif "not declared" in message.lower() or "cannot find symbol" in message.lower():
                error_type = "NameError"
                
    return error_type, message


def generate_quick_fix(language, error_type, message):
    if language == "python":
        if error_type == "NameError":
            var = message.split("'")[1] if "'" in message else "x"
            return f"{var} = 0\nprint({var})"
        if error_type == "SyntaxError":
            return "Check missing ':' or brackets"
            
    elif language == "cpp":
        if "not declared" in message: return "Declare variable before use"
        if "expected" in message: return "Check missing ; or {}"
        
    elif language == "java":
        if "cannot find symbol" in message: return "Declare variable or import class"
        if "missing return statement" in message: return "Add return statement"
        
    elif language == "javascript":
        if "is not defined" in message: return "Declare variable using let/const"
        
    return None


def parse_error(language, error_output, code=None):
    result = {
        "language": language,
        "error_type": "Unknown Error",
        "line_number": None,
        "column_number": None,
        "message": "",
        "meaning": "An execution error occurred.",
        "suggestion": "Check the code syntax and logic around the reported line.",
        "error_line_content": "",
        "resolved_code": None,
        "quick_fix": None
    }
    
    if not error_output or not error_output.strip():
        return result
        
    # Extract line and column
    line_no, col_no = extract_line_and_column(language, error_output)
    result["line_number"] = line_no
    result["column_number"] = col_no
    
    # Extract error type and message
    err_type, err_msg = extract_error_details(language, error_output)
    result["error_type"] = err_type
    result["message"] = err_msg
    
    # Meaning + Suggestion
    meaning, suggestion = explain_error(language, err_type, err_msg)
    result["meaning"] = meaning
    result["suggestion"] = suggestion
    
    # Quick fix compatibility
    result["quick_fix"] = generate_quick_fix(language, err_type, err_msg)
    
    # Error line content
    if code and line_no:
        code_lines = code.splitlines()
        if 1 <= line_no <= len(code_lines):
            result["error_line_content"] = code_lines[line_no - 1]
            
    # Resolve the code
    if code and line_no:
        resolved = resolve_error(code, language, err_type, err_msg, line_no, col_no)
        result["resolved_code"] = resolved
        
    return result