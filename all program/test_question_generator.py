from question_generator import save_question


question = {
    "question": "What does SQL stand for?",
    "option_a": "Structured Query Language",
    "option_b": "Simple Question Language",
    "option_c": "System Query Logic",
    "option_d": "Structured Question Logic",
    "correct_answer": "A",
    "explanation": "SQL stands for Structured Query Language.",
    "difficulty": "Easy",
    "question_type": "MCQ"
}


question_id = save_question(question)

if question_id:
    print("Test completed successfully.")
else:
    print("Test failed.")