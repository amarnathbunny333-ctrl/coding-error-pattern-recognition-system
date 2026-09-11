from backend.language_detector import detect_language

print(detect_language("print(x)"))
print(detect_language("#include<iostream>"))
print(detect_language("public class Main {}"))
print(detect_language("console.log(x)"))