from result_service import calculate_result


result = calculate_result(
    test_id=1,
    student_email="student@example.com"
)

if result:
    print("\nRESULT")
    print("--------------------")
    print("Total:", result["total_questions"])
    print("Correct:", result["correct_answers"])
    print("Incorrect:", result["incorrect_answers"])
    print("Unattempted:", result["unattempted"])
    print("Score:", result["score"])
    print("Percentage:", result["percentage"])
else:
    print("Result calculation failed.")