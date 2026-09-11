# 🚀 Coding Error Pattern Recognition System

An intelligent, AI-powered full-stack web platform designed to analyze multi-language source code, execute code in a sandboxed environment, detect compilation and runtime errors, recognize error patterns, and provide automated AI-driven explanations and code fixes.

---

## 🌟 Key Features

- **⚡ Multi-Language Compiler Engine**: Executes Python, C++, Java, and JavaScript code in a controlled sandboxed subprocess with timeout and resource handling.
- **🔍 Automated Language & Error Detection**: Automatically identifies source code language and parses error messages (line number, error type, and raw traceback).
- **🤖 LLM AI Diagnostics & Auto-Fix**: Powered by Groq API (`llama-3.1-8b-instant`) to deliver beginner-friendly error explanations, actionable suggestions, and auto-generated corrected code blocks.
- **💬 Interactive AI Debugging Chatbot**: Context-aware AI assistant that understands your active code workspace and terminal output to answer debugging questions.
- **🎤 Voice Input & Speech Explanations**: Supports voice-to-text queries via the Web Speech API and text-to-speech voice narration for error explanations.
- **📊 Real-Time Analytics & Run History**: Tracks execution metrics, total errors analyzed, most/least frequent error types, and run logs.
- **📄 Report Generation Suite**: Includes Markdown and automated Microsoft Word (`.docx`) report generation tools for academic and mini-project literature reviews.

---

## 🛠️ Technology Stack

- **Backend**: Python 3, Flask, Groq API (Llama 3.1), Subprocess Sandbox Engine
- **Frontend**: HTML5, Vanilla CSS3 (Modern Dark Mode UI & Glassmorphism Design Tokens), JavaScript (Fetch API, Web Speech API)
- **Document Utilities**: `python-docx` for `.docx` report generation

---

## 📁 Project Structure

```text
CodingErrorPetternRecognitiomSystem/
├── app.py                      # Flask Application Server & Web API Endpoints
├── requirements.txt            # Python Dependencies
├── README.md                   # Project Documentation
├── backend/                    # Core Execution Engine & Analytics Modules
│   ├── analyzer.py             # Analysis coordinator
│   ├── compiler_engine.py      # Subprocess compiler/interpreter runner (Python, C++, Java, JS)
│   ├── error_parser.py         # Structured error regex parser & extractor
│   ├── error_patterns.py       # Knowledge base of standard error patterns & hints
│   ├── history_store.py        # Persistence layer for run history
│   ├── language_detector.py    # Source code language identification module
│   ├── statistics.py           # Error frequency calculator & analytics generator
│   ├── test_compiler_engine.py # Test suite for compiler engine
│   ├── test_error_parser.py    # Test suite for error parsing
│   └── test_language_detector.py # Test suite for language detector
├── reports/                    # Documentation source & report builder script
│   ├── Literature_Review_Report.md
│   └── generate_docx.py
├── static/                     # Static media & downloadable report assets
│   └── Literature_Review_Report.docx
└── templates/                  # Web Interface Templates
    └── index.html              # Main IDE, AI Chat & Analytics Web Interface
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have Python 3.8+ installed along with compilers for any languages you wish to execute locally:
- Python 3
- GCC / G++ (for C++)
- JDK / Java (for Java)
- Node.js (for JavaScript)

### 2. Installation & Setup
Clone the repository and install the dependencies:
```bash
git clone https://github.com/amarnathbunny333-ctrl/coding-error-pattern-recognition-system.git
cd coding-error-pattern-recognition-system

# Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables (Optional for AI Features)
Set your Groq API Key to enable AI-powered explanations, smart auto-fixes, and the chatbot:
```bash
# On Windows PowerShell:
$env:GROQ_API_KEY="your_groq_api_key_here"

# On Linux/macOS:
export GROQ_API_KEY="your_groq_api_key_here"
```

### 4. Running the Application
Launch the Flask application:
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 🧪 Running Tests

Execute the backend test suites to verify system functionality:
```bash
python backend/test_compiler_engine.py
python backend/test_error_parser.py
python backend/test_language_detector.py
```

---

## 👤 Author

**Amarnath**  
GitHub: [@amarnathbunny333-ctrl](https://github.com/amarnathbunny333-ctrl)