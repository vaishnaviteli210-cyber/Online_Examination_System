from question_generator import save_question


mcq = {
    "question": "What is Python?",
    "option_a": "Programming language",
    "option_b": "Database",
    "option_c": "Operating system",
    "option_d": "Web browser",
    "correct_answer": "A",
    "explanation": "Python is a programming language.",
    "difficulty": "Easy",
    "question_type": "MCQ"
}


question_id = save_question(mcq)

if question_id:
    print("MCQ saved successfully.")
else:
    print("MCQ save failed.")