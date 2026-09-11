# Mini Project Literature Review Report On
# CODING ERROR PATTERN RECOGNITION SYSTEM

**Submitted by**
* **MUKKERA VISHAL** &emsp; 22R11A66H5
* **O VASANTH KUMAR** &ensp; 22R11A66H7
* **PATNAPU SAI PAVAN** &nbsp; 22R11A66J2

**Under the guidance of**
* **M.SIVA PRASAD**
* Assistant Professor, CSE(AIML) Department
* Geethanjali College Of Engineering and Technology

---

## Index

* **Abstract** ................................................................................................... **1**
* **1. Introduction** ........................................................................................ **2**
  * 1.1 About the project ............................................................................... **2**
  * 1.2 Problem Statement ............................................................................. **2**
  * 1.3 Project Objectives .............................................................................. **3**
* **2. Literature Review** .................................................................................. **4**
  * 2.1 Existing work .................................................................................... **4**
  * 2.2 Research Papers ................................................................................ **5**
  * 2.3 Limitations of Existing Work .............................................................. **6**

---

<div style="page-break-after: always;"></div>

## Abstract

**Coding Error Pattern Recognition System** is an AI-powered developer tool designed to enhance the programming learning curve by providing intelligent, interactive code execution feedback. At its core, the system integrates a multi-language runner engine (supporting Python, C++, Java, and JavaScript) with a Generative AI backend (LLM-based) powered by Groq. When a user runs code that fails to compile or execute, the system automatically intercepts the console tracebacks and performs localization to isolate the exact error row (line) and column. It then forwards the program context and execution traces to a Large Language Model (LLM) to generate a structured debugging analysis containing a beginner-friendly explanation of the error pattern, an actionable suggestion, and the fully corrected source code. 

By combining real-time multi-language sandboxed execution, regex-based error positioning, and generative program repair, the system functions as a personal programming tutor. Unlike conventional Integrated Development Environments (IDEs) which output cryptic, intimidating compiler errors, this platform provides an interactive "Apply Resolution" interface, letting developers immediately correct their code with a single click. This project demonstrates how modern conversational AI can be integrated into compiler toolchains to bridge the gap between error detection and program repair, reducing cognitive fatigue and fostering autonomous debugging skills.

---

<div style="page-break-after: always;"></div>

## 1. Introduction

### 1.1 About the Project
**Coding Error Pattern Recognition System** is an interactive web-based workbench that acts as a smart debugger. It detects code languages, compiles/runs programs in a sandboxed execution layer, parses tracebacks to locate faults, and consults an LLM in real-time to explain and resolve the errors. 

Unlike traditional compilers that only present raw error dumps, this system parses line numbers, column points, and error names, and translates them into understandable explanations. The application features an intuitive, glassmorphic web-based interface where users can:
* Write and execute code across four major programming languages (Python, C++, Java, JavaScript).
* View precise visual indicators showing exactly which line and column triggered the exception.
* Receive clear, non-cryptic error explanations and actionable suggestions.
* Apply suggested code corrections immediately with a one-click **Apply Resolution** control.
* Converse with an AI Coding Assistant for further educational explanations.

The system is particularly suited for CS students, novice developers, and educators. By combining sandboxed compiler engines with generative program repair, the system transitions compilers from passive detectors into active, educational repair assistants.

### 1.2 Problem Statement
Novice programmers struggle significantly with interpreting compiler and interpreter feedback. Traditional error outputs—such as C++ template messages, Java stack traces, and JavaScript runtime errors—are frequently long, cryptic, and intimidating, causing cognitive fatigue and slowing down the learning loop.

Moreover, existing programming assistants are fragmented: static linters (like ESLint or Pylint) detect errors but fail to run the program; standard sandboxed runtimes execute code but do not explain crashes; and generic chat engines (like ChatGPT or Gemini) require manual copying-and-pasting of code and errors, lacking immediate execution feedback. This creates a clear gap for an integrated, interactive system that automatically executes code, maps execution failures, and resolves errors in place.

---

<div style="page-break-after: always;"></div>

### 1.3 Project Objectives
The key objectives of the Coding Error Pattern Recognition System are:
1. **Multi-Language Execution Sandbox** – Provide a secure sandbox to compile and execute Python, C++, Java, and JavaScript programs in real-time.
2. **Error Localization (Row & Column)** – Build custom parsers and caret line tracking algorithms to isolate the exact line (row) and column causing syntax or compilation errors.
3. **Automated Generative Analysis** – Establish an automated background pipeline that sends error tracebacks and code context to a Large Language Model (Groq/Llama) to obtain structured JSON containing user-friendly explanations and suggested fixes.
4. **Interactive Program Repair** – Implement a one-click code resolution interface in the web editor to allow developers to automatically apply the generated fix and re-run.
5. **Interactive Coding Chat & Statistics Dashboard** – Provide a comprehensive dashboard featuring historical error statistics and a voice-enabled AI Chat assistant to explain coding concepts dynamically.

---

<div style="page-break-after: always;"></div>

## 2. Literature Survey

### 2.1 Existing Work

#### 1. Static Linters and Static Program Analyzers
Traditional static linters (e.g., Pylint, ESLint, cppcheck) scan source code for structural anomalies, syntax issues, and anti-patterns without actually running the files. While they are quick at detecting basic typos, they cannot trace dynamic runtime errors (e.g., index out of bounds, null pointer exceptions, division by zero) and do not provide interactive code fixes.

#### 2. Compiler Tracebacks and IDE Highlights
Modern IDEs (like VS Code, Eclipse, or PyCharm) integrate compilers that underline errors and display tracebacks. However, these tools simply mirror raw outputs from the underlying compiler (e.g. GCC/Clang or Java Virtual Machine). For beginner programmers, these raw tracebacks remain overly technical and lack friendly tutorials.

#### 3. Traditional Automated Program Repair (APR)
Traditional APR research uses search-based or constraint-based techniques (such as genetic programming) to automatically patch programs. These systems require extensive test suites to validate patches and are computationally heavy, limiting their deployment in student-facing applications or web browsers.

#### 4. Generic Conversational AI Assistants
Generative AI tools (like ChatGPT, Claude) have been used extensively to debug code. However, they are isolated from the code editor: programmers must manually copy their code, paste the traceback, submit it, and then manually copy the correction back into their editor. This creates a fragmented UX with high friction.

---

<div style="page-break-after: always;"></div>

### 2.2 Research Papers

#### 1. HelpMeOut: Remedying Compiler Errors Using Crowd-Sourced Search
* **Authors**: Björn Hartmann, Daniel MacDougall, Joel Brandt, Scott R. Klemmer (ACM CHI, 2010).
* **Summary**: HelpMeOut assists programmers in debugging compiler errors by suggesting solutions that have worked for other programmers. It records code edits associated with compilation success and indexes them. When a user hits an error, the system performs diff-matching and suggests fixes.
* **Why it matters for this Project**: Demonstrates that matching compiler errors directly to concrete code edits dramatically accelerates learning. Our system builds on this by generating the fix dynamically using an LLM, removing the need for a static database of historical diffs.

#### 2. An Empirical Study of Compiler Error Message Usability
* **Authors**: Titus Barik et al. (IEEE SIGCSE, 2016).
* **Summary**: This study assesses compiler error messages from a human-computer interaction (HCI) perspective. The results show that cryptic terminology, lack of visual localization (such as exact lines and columns), and absence of actionable "quick-fixes" are the primary causes of developer frustration.
* **Why it matters for this Project**: Validates the core UX hypothesis of our system—highlighting that row/column indicators, plain-language "meanings", and a direct **Apply Resolution** workflow are essential for student success.

#### 3. Self-Debugging: Large Language Models for Automated Code Debugging
* **Authors**: Xinyun Chen et al. (arXiv, 2023).
* **Summary**: The paper introduces "Self-Debugging", where an LLM is taught to debug its code by analyzing interpreter feedback. By feeding error tracebacks back into the context loop, the model self-identifies syntax and logic bugs.
* **Why it matters for this Project**: Confirms that giving the LLM both the source code and raw compiler tracebacks leads to highly accurate patch generation. We employ this feedback loop to drive our `/analyze` backend route.

#### 4. Automated Program Repair in the Era of Large Language Models
* **Authors**: Chunqiu Steven Xia and David Lo (Preprint, 2024).
* **Summary**: This paper benchmarks the effectiveness of instruction-following LLMs for patching code bugs in Python, Java, and C++. It demonstrates that prompting models for structured code modifications generates high-quality compilable code.
* **Why it matters for this Project**: Informed the prompt structure inside `app.py`, establishing the JSON output format constraint to ensure the LLM returns parsing-friendly structures.

---

<div style="page-break-after: always;"></div>

### 2.3 Limitations of Existing Work

While previous research and IDEs offer helpful diagnostic tools, gaps remain in delivering a cohesive, educational environment for student developers:
1. **Cryptic Diagnostics**: Compilers focus on technical soundness, producing outputs like `error: expected constructor, destructor, or type conversion` that confuse novices.
2. **Fragmented Workflows**: Programmers must jump between compiler terminals, stack traces, and search engines, losing focus.
3. **No Direct Editor Resolution**: Standard diagnostic systems report errors but do not offer direct in-editor patching, requiring the programmer to manually implement the solution.
4. **Lack of Educational Explanations**: IDEs offer quick-fixes for trivial formatting (e.g. imports), but do not explain *why* the error occurred or what the pattern means.

**Coding Error Pattern Recognition System** addresses these limitations by uniting a multi-language compiler runner, custom error localization, and an LLM-based program debugger into a single interface. When code fails, the user gets localized markers, clear explanations, and an active **Apply Resolution** button that automatically patches and runs their program.
