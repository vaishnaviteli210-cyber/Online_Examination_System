from test_service import create_test


def get_positive_number(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def create_exam_from_user():

    print("\n==============================")
    print("      ONLINE EXAM SYSTEM")
    print("==============================")

    # Test name
    test_name = input("Enter test name: ").strip()

    while not test_name:
        print("Test name cannot be empty.")
        test_name = input("Enter test name: ").strip()

    # Student email
    student_email = input("Enter student email: ").strip()

    while not student_email:
        print("Student email cannot be empty.")
        student_email = input("Enter student email: ").strip()

    # Number of questions
    number_of_questions = get_positive_number(
        "How many questions do you want? "
    )

    # Difficulty
    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty_choice = input("Enter choice: ")

    difficulty_map = {
        "1": "Easy",
        "2": "Medium",
        "3": "Hard"
    }

    while difficulty_choice not in difficulty_map:
        print("Invalid choice.")
        difficulty_choice = input("Enter choice: ")

    difficulty = difficulty_map[difficulty_choice]

    # Question type
    print("\nChoose question type:")
    print("1. MCQ")

    question_type_choice = input("Enter choice: ")

    while question_type_choice != "1":
        print("Invalid choice.")
        question_type_choice = input("Enter choice: ")

    question_type = "MCQ"

    # Time limit
    time_limit = get_positive_number(
        "Enter time limit in minutes: "
    )

    print("\nCreating your test...")

    test_id = create_test(
        test_name=test_name,
        student_email=student_email,
        number_of_questions=number_of_questions,
        difficulty=difficulty,
        question_type=question_type,
        time_limit=time_limit
    )

    if test_id:
        print("\n==============================")
        print("Test created successfully!")
        print("Test ID:", test_id)
        print("==============================")

    else:
        print("\nTest could not be created.")


if __name__ == "__main__":
    create_exam_from_user()