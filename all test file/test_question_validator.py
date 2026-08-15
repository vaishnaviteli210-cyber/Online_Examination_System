from question_validator import validate_question


question = {
    "question": "What is Python?",
    "option_a": "Programming language",
    "option_b": "Database",
    "option_c": "Operating system",
    "option_d": "Web browser",
    "correct_answer": "A",
    "difficulty": "Easy"
}


valid, message = validate_question(question)

print(message)