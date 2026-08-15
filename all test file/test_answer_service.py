from answer_service import submit_answer


result = submit_answer(
    test_id=1,
    question_id=1,
    student_email="student@example.com",
    selected_answer="A"
)

if result:
    print("Answer test passed.")
else:
    print("Answer test failed.")