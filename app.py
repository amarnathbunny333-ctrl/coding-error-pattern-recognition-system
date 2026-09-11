import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

from backend.language_detector import detect_language
from backend.compiler_engine import (
    run_python,
    run_cpp,
    run_java,
    run_javascript
)
from backend.error_parser import parse_error
from backend.statistics import save_error, get_statistics
from backend.history_store import save_history, get_history

app = Flask(__name__)

# =========================
# 🔑 GROQ CLIENT
# =========================
client = Groq(api_key=os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY"))


# =========================
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# ANALYZE CODE
# =========================
@app.route("/analyze", methods=["POST"])
def analyze():

    code = request.form.get("code", "")

    language = detect_language(code)

    if language == "python":
        result = run_python(code)
    elif language == "cpp":
        result = run_cpp(code)
    elif language == "java":
        result = run_java(code)
    elif language == "javascript":
        result = run_javascript(code)
    else:
        return jsonify({
            "language": language,
            "output": "Unsupported language",
            "success": False
        })

    response = {
        "language": language,
        "output": result.get("output", ""),
        "success": result.get("success", False)
    }

    # error analysis
    if not response["success"]:
        parsed = parse_error(language, response["output"], code=code)
        
        # Automatically consult the LLM for explanations and fixes
        try:
            prompt = f"""
Language: {language}
Error Output:
{response['output']}

Source Code:
{code}

Analyze the compiler/interpreter error and code, then provide a JSON object with:
- "meaning": a clear, beginner-friendly explanation of why this error occurred.
- "suggestion": a specific, direct suggestion on how to fix this error.
- "resolved_code": the complete corrected code with the error resolved. Return the raw code block as a string. Do not wrap the code block in markdown code fences inside the JSON string.
"""
            llm_response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system",
                        "content": "You are a smart AI debugger. You must analyze the error and respond ONLY with a valid JSON object matching the requested schema."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            import json
            llm_data = json.loads(llm_response.choices[0].message.content)
            if llm_data.get("meaning"):
                parsed["meaning"] = llm_data["meaning"]
            if llm_data.get("suggestion"):
                parsed["suggestion"] = llm_data["suggestion"]
            if llm_data.get("resolved_code"):
                parsed["resolved_code"] = llm_data["resolved_code"]
        except Exception as e:
            print("LLM Debugger Error:", e)

        response["analysis"] = parsed
        save_error(parsed)
        response["stats"] = get_statistics()

    save_history(response)

    return jsonify(response)


# =========================
# HISTORY
# =========================
@app.route("/history")
def history():
    return jsonify(get_history())


# =========================
# 🤖 CHAT (SAFE GROQ)
# =========================
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json or {}
    msg = data.get("message", "")
    code = data.get("code", "")
    error = data.get("error", "")

    # Build contextual system prompt
    system_content = "You are a smart AI coding assistant. Help debug code and explain errors clearly."
    if code or error:
        system_content += "\n\nContext of the user's workspace:"
        if code:
            system_content += f"\n--- CURRENT CODE IN WORKSPACE ---\n{code}"
        if error and error != "Terminal output will be displayed here...":
            system_content += f"\n--- CURRENT ERROR IN WORKSPACE ---\n{error}"

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": system_content
                },
                {
                    "role": "user",
                    "content": msg
                }
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Groq API Error: {str(e)}"})

# =========================
# 🛠 AUTO FIX ENGINE (SAFE)
# =========================
@app.route("/auto-fix", methods=["POST"])
def auto_fix():

    code = request.json.get("code", "")

    if not code:
        return jsonify({"fixed": "", "message": "No code received"})

    fixed = code

    # Python fixes
    if "for " in code and ":" not in code:
        fixed += ":"

    # C/C++ fixes
    if ("cout" in code or "printf" in code) and ";" not in code:
        fixed += ";"

    # indentation fix
    fixed = fixed.replace("\t", "    ")

    return jsonify({
        "fixed": fixed,
        "message": "Auto-fix applied successfully"
    })

# =========================
# ▶ RUN CODE
# =========================

@app.route("/run", methods=["POST"])
def run_code():

    code = request.json.get("code", "")
    language = request.json.get("language", "")

    if language == "python":
        result = run_python(code)

    elif language == "cpp":
        result = run_cpp(code)

    elif language == "java":
        result = run_java(code)

    elif language == "javascript":
        result = run_javascript(code)

    else:
        return jsonify({
            "success": False,
            "output": "Unsupported language"
        })

    return jsonify(result)
# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)