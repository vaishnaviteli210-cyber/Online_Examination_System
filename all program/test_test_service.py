from test_service import create_test


test_id = create_test(
    test_name="Python Basics",
    student_email="student@example.com",
    number_of_questions=2,
    difficulty="Easy",
    question_type="MCQ",
    time_limit=20
)

if test_id:
    print("Test creation test passed.")
else:
    print("Test creation test failed.")