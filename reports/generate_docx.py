import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_report():
    doc = docx.Document()
    
    # Page setup
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
    # Styles Setup
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Arial'
    font.size = Pt(11)
    font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    
    # ------------------ COVER PAGE ------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    run_space = p.add_run("\n\nMini Project Literature Review Report On\n\n")
    run_space.font.size = Pt(16)
    run_space.font.bold = True
    run_space.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    run_title = p.add_run("CODING ERROR PATTERN RECOGNITION SYSTEM\n\n\n")
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0x3b, 0x82, 0xf6) # Blue Accent
    
    run_sub = p.add_run("Submitted by\n")
    run_sub.font.size = Pt(12)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0xef, 0x44, 0x44) # Red
    
    run_auths = p.add_run("MUKKERA VISHAL &emsp; 22R11A66H5\nO VASANTH KUMAR &ensp; 22R11A66H7\nPATNAPU SAI PAVAN &nbsp; 22R11A66J2\n\n\n")
    run_auths.font.size = Pt(12)
    run_auths.font.bold = True
    run_auths.font.color.rgb = RGBColor(0xef, 0x44, 0x44)
    
    run_guide_title = p.add_run("Under the guidance of\n")
    run_guide_title.font.size = Pt(12)
    run_guide_title.font.bold = True
    run_guide_title.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    run_guide = p.add_run("M.SIVA PRASAD\nAssistant Professor, CSE(AIML) Department\nGeethanjali College Of Engineering and Technology\n")
    run_guide.font.size = Pt(12)
    run_guide.font.bold = True
    run_guide.font.color.rgb = RGBColor(0x3b, 0x82, 0xf6)
    
    doc.add_page_break()
    
    # ------------------ INDEX PAGE ------------------
    p_index = doc.add_paragraph()
    p_index.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_idx_title = p_index.add_run("Index\n\n")
    run_idx_title.font.size = Pt(18)
    run_idx_title.font.bold = True
    
    items = [
        ("Abstract", "1"),
        ("1. Introduction", "2"),
        ("   1.1 About the project", "2"),
        ("   1.2 Problem Statement", "2"),
        ("   1.3 Project Objectives", "3"),
        ("2. Literature Review", "4"),
        ("   2.1 Existing work", "4"),
        ("   2.2 Research Papers", "5"),
        ("   2.3 Limitations of Existing Work", "6"),
    ]
    
    for item, page in items:
        p_item = doc.add_paragraph()
        lead_len = 65 - len(item) - len(page)
        dots = "." * max(5, lead_len)
        p_item.add_run(f"{item} {dots} {page}").font.size = Pt(11)
        
    doc.add_page_break()
    
    # ------------------ ABSTRACT ------------------
    h_abs = doc.add_paragraph()
    r = h_abs.add_run("ABSTRACT")
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x3b, 0x82, 0xf6)
    h_abs.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p_abs = doc.add_paragraph(
        "Coding Error Pattern Recognition System is an AI-powered developer tool designed to enhance the programming learning curve by providing intelligent, interactive code execution feedback. At its core, the system integrates a multi-language runner engine (supporting Python, C++, Java, and JavaScript) with a Generative AI backend (LLM-based) powered by Groq. When a user runs code that fails to compile or execute, the system automatically intercepts the console tracebacks and performs localization to isolate the exact error row (line) and column. It then forwards the program context and execution traces to a Large Language Model (LLM) to generate a structured debugging analysis containing a beginner-friendly explanation of the error pattern, an actionable suggestion, and the fully corrected source code."
    )
    p_abs.paragraph_format.line_spacing = 1.15
    p_abs.paragraph_format.space_after = Pt(12)
    
    p_abs2 = doc.add_paragraph(
        "By combining real-time multi-language sandboxed execution, regex-based error positioning, and generative program repair, the system functions as a personal programming tutor. Unlike conventional Integrated Development Environments (IDEs) which output cryptic, intimidating compiler errors, this platform provides an interactive \"Apply Resolution\" interface, letting developers immediately correct their code with a single click. This project demonstrates how modern conversational AI can be integrated into compiler toolchains to bridge the gap between error detection and program repair, reducing cognitive fatigue and fostering autonomous debugging skills."
    )
    p_abs2.paragraph_format.line_spacing = 1.15
    p_abs2.paragraph_format.space_after = Pt(12)
    
    doc.add_page_break()
    
    # ------------------ INTRODUCTION ------------------
    h_intro = doc.add_paragraph()
    r = h_intro.add_run("1. Introduction")
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x3b, 0x82, 0xf6)
    
    # 1.1 About
    h_about = doc.add_paragraph()
    r = h_about.add_run("\n1.1 About the Project")
    r.font.size = Pt(14)
    r.font.bold = True
    
    p_about = doc.add_paragraph(
        "Coding Error Pattern Recognition System is an interactive web-based workbench that acts as a smart debugger. It detects code languages, compiles/runs programs in a sandboxed execution layer, parses tracebacks to locate faults, and consults an LLM in real-time to explain and resolve the errors."
    )
    p_about.paragraph_format.space_after = Pt(6)
    
    doc.add_paragraph("The application features an intuitive web-based interface where users can:")
    doc.add_paragraph("• Write and execute code across four major programming languages (Python, C++, Java, JavaScript).", style='List Bullet')
    doc.add_paragraph("• View precise visual indicators showing exactly which line and column triggered the exception.", style='List Bullet')
    doc.add_paragraph("• Receive clear, non-cryptic error explanations and actionable suggestions.", style='List Bullet')
    doc.add_paragraph("• Apply suggested code corrections immediately with a one-click Apply Resolution control.", style='List Bullet')
    doc.add_paragraph("• Converse with an AI Coding Assistant for further educational explanations.", style='List Bullet')
    
    p_about_end = doc.add_paragraph(
        "\nThe system is particularly suited for CS students, novice developers, and educators. By combining sandboxed compiler engines with generative program repair, the system transitions compilers from passive detectors into active, educational repair assistants."
    )
    p_about_end.paragraph_format.space_after = Pt(12)
    
    # 1.2 Problem Statement
    h_prob = doc.add_paragraph()
    r = h_prob.add_run("\n1.2 Problem Statement")
    r.font.size = Pt(14)
    r.font.bold = True
    
    p_prob = doc.add_paragraph(
        "Novice programmers struggle significantly with interpreting compiler and interpreter feedback. Traditional error outputs—such as C++ template messages, Java stack traces, and JavaScript runtime errors—are frequently long, cryptic, and intimidating, causing cognitive fatigue and slowing down the learning loop."
    )
    p_prob.paragraph_format.space_after = Pt(6)
    p_prob2 = doc.add_paragraph(
        "Moreover, existing programming assistants are fragmented: linters detect errors but fail to run code; standard sandboxed runtimes execute code but do not explain crashes; and generic chat engines require manual copying-and-pasting of code and errors, lacking immediate execution feedback. This creates a clear gap for an integrated, interactive system that automatically executes code, maps execution failures, and resolves errors in place."
    )
    p_prob2.paragraph_format.space_after = Pt(12)
    
    # 1.3 Objectives
    h_obj = doc.add_paragraph()
    r = h_obj.add_run("\n1.3 Project Objectives")
    r.font.size = Pt(14)
    r.font.bold = True
    
    doc.add_paragraph("The key objectives of the Coding Error Pattern Recognition System are:")
    doc.add_paragraph("1. Multi-Language Execution Sandbox – Provide a secure sandbox to compile and execute Python, C++, Java, and JavaScript programs in real-time.", style='List Number')
    doc.add_paragraph("2. Error Localization (Row & Column) – Build custom parsers and caret line tracking algorithms to isolate the exact line (row) and column causing syntax or compilation errors.", style='List Number')
    doc.add_paragraph("3. Automated Generative Analysis – Establish an automated background pipeline that sends error tracebacks and code context to a Large Language Model (Groq/Llama) to obtain structured JSON containing user-friendly explanations and suggested fixes.", style='List Number')
    doc.add_paragraph("4. Interactive Program Repair – Implement a one-click code resolution interface in the web editor to allow developers to automatically apply the generated fix and re-run.", style='List Number')
    doc.add_paragraph("5. Interactive Coding Chat & Statistics Dashboard – Provide a comprehensive dashboard featuring historical error statistics and a voice-enabled AI Chat assistant to explain coding concepts dynamically.", style='List Number')
    
    doc.add_page_break()
    
    # ------------------ LITERATURE REVIEW ------------------
    h_lit = doc.add_paragraph()
    r = h_lit.add_run("2. Literature Review")
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x3b, 0x82, 0xf6)
    
    # 2.1 Existing Work
    h_exist = doc.add_paragraph()
    r = h_exist.add_run("\n2.1 Existing Work")
    r.font.size = Pt(14)
    r.font.bold = True
    
    doc.add_paragraph("1. Static Linters and Static Program Analyzers", style='List Number')
    doc.add_paragraph("Traditional static linters (e.g., Pylint, ESLint, cppcheck) scan source code for structural anomalies, syntax issues, and anti-patterns without actually running the files. While they are quick at detecting basic typos, they cannot trace dynamic runtime errors (e.g., index out of bounds, null pointer exceptions, division by zero) and do not provide interactive code fixes.")
    
    doc.add_paragraph("2. Compiler Tracebacks and IDE Highlights", style='List Number')
    doc.add_paragraph("Modern IDEs (like VS Code, Eclipse, or PyCharm) integrate compilers that underline errors and display tracebacks. However, these tools simply mirror raw outputs from the underlying compiler (e.g. GCC/Clang or Java Virtual Machine). For beginner programmers, these raw tracebacks remain overly technical and lack friendly tutorials.")
    
    doc.add_paragraph("3. Traditional Automated Program Repair (APR)", style='List Number')
    doc.add_paragraph("Traditional APR research uses search-based or constraint-based techniques (such as genetic programming) to automatically patch programs. These systems require extensive test suites to validate patches and are computationally heavy, limiting their deployment in student-facing applications or web browsers.")
    
    doc.add_paragraph("4. Generic Conversational AI Assistants", style='List Number')
    doc.add_paragraph("Generative AI tools (like ChatGPT, Claude) have been used extensively to debug code. However, they are isolated from the code editor: programmers must manually copy their code, paste the traceback, submit it, and then manually copy the correction back into their editor. This creates a fragmented UX with high friction.")
    
    # 2.2 Research Papers
    h_papers = doc.add_paragraph()
    r = h_papers.add_run("\n2.2 Research Papers")
    r.font.size = Pt(14)
    r.font.bold = True
    
    papers_data = [
        ("1. HelpMeOut: Remedying Compiler Errors Using Crowd-Sourced Search", 
         "Björn Hartmann, Daniel MacDougall, Joel Brandt, Scott R. Klemmer (ACM CHI, 2010).",
         "HelpMeOut assists programmers in debugging compiler errors by suggesting solutions that have worked for other programmers. It records code edits associated with compilation success and indexes them. When a user hits an error, the system performs diff-matching and suggests fixes.",
         "Demonstrates that matching compiler errors directly to concrete code edits dramatically accelerates learning. Our system builds on this by generating the fix dynamically using an LLM, removing the need for a static database of historical diffs."),
        ("2. An Empirical Study of Compiler Error Message Usability",
         "Titus Barik et al. (IEEE SIGCSE, 2016).",
         "This study assesses compiler error messages from a human-computer interaction (HCI) perspective. The results show that cryptic terminology, lack of visual localization (such as exact lines and columns), and absence of actionable 'quick-fixes' are the primary causes of developer frustration.",
         "Validates the core UX hypothesis of our system—highlighting that row/column indicators, plain-language 'meanings', and a direct Apply Resolution workflow are essential for student success."),
        ("3. Self-Debugging: Large Language Models for Automated Code Debugging",
         "Xinyun Chen et al. (arXiv, 2023).",
         "The paper introduces 'Self-Debugging', where an LLM is taught to debug its code by analyzing interpreter feedback. By feeding error tracebacks back into the context loop, the model self-identifies syntax and logic bugs.",
         "Confirms that giving the LLM both the source code and raw compiler tracebacks leads to highly accurate patch generation. We employ this feedback loop to drive our /analyze backend route."),
        ("4. Automated Program Repair in the Era of Large Language Models",
         "Chunqiu Steven Xia and David Lo (Preprint, 2024).",
         "This paper benchmarks the effectiveness of instruction-following LLMs for patching code bugs in Python, Java, and C++. It demonstrates that prompting models for structured code modifications generates high-quality compilable code.",
         "Informed the prompt structure inside app.py, establishing the JSON output format constraint to ensure the LLM returns parsing-friendly structures.")
    ]
    
    for title, auth, summ, why in papers_data:
        p_title = doc.add_paragraph()
        r_title = p_title.add_run(f"\n{title}")
        r_title.font.bold = True
        r_title.font.size = Pt(12)
        
        doc.add_paragraph(f"• Author: {auth}")
        doc.add_paragraph(f"• Summary: {summ}")
        doc.add_paragraph(f"• Why it matters for this Project: {why}")
        
    # 2.3 Limitations of Existing Work
    h_limits = doc.add_paragraph()
    r = h_limits.add_run("\n2.3 Limitations of Existing Work")
    r.font.size = Pt(14)
    r.font.bold = True
    
    doc.add_paragraph("While previous research and IDEs offer helpful diagnostic tools, gaps remain in delivering a cohesive, educational environment for student developers:")
    doc.add_paragraph("1. Cryptic Diagnostics: Compilers focus on technical soundness, producing outputs like error: expected constructor, destructor, or type conversion that confuse novices.", style='List Bullet')
    doc.add_paragraph("2. Fragmented Workflows: Programmers must jump between compiler terminals, stack traces, and search engines, losing focus.", style='List Bullet')
    doc.add_paragraph("3. No Direct Editor Resolution: Standard diagnostic systems report errors but do not offer direct in-editor patching, requiring the programmer to manually implement the solution.", style='List Bullet')
    doc.add_paragraph("4. Lack of Educational Explanations: IDEs offer quick-fixes for trivial formatting (e.g. imports), but do not explain why the error occurred or what the pattern means.", style='List Bullet')
    
    p_limits_end = doc.add_paragraph(
        "\nCoding Error Pattern Recognition System addresses these limitations by uniting a multi-language compiler runner, custom error localization, and an LLM-based program debugger into a single interface. When code fails, the user gets localized markers, clear explanations, and an active Apply Resolution button that automatically patches and runs their program."
    )
    p_limits_end.paragraph_format.space_after = Pt(12)
    
    # Save document to the static folder for web serving/download
    os.makedirs("static", exist_ok=True)
    file_path = "static/Literature_Review_Report.docx"
    doc.save(file_path)
    print(f"Report generated successfully at {file_path}")

if __name__ == "__main__":
    create_report()
