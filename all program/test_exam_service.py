from exam_service import get_test_questions


test_id = 1

questions = get_test_questions(test_id)

if questions:
    print(f"Found {len(questions)} questions.")

    for question in questions:
        print()
        print("Question:", question["question"])
        print("A:", question["option_a"])
        print("B:", question["option_b"])
        print("C:", question["option_c"])
        print("D:", question["option_d"])
else:
    print("No questions found.")