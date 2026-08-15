from document_reader import extract_text
from generate_and_save import generate_and_save
from test_service import create_test
from exam_service import get_test_questions
from answer_service import submit_answer
from result_service import calculate_result


def choose_question_type():
    print("\nQuestion type:")
    print("1. MCQ")
    print("2. Theory")
    print("3. Both")

    while True:
        choice = input("Choose: ")

        types = {
            "1": "MCQ",
            "2": "Theory",
            "3": "Both"
        }

        if choice in types:
            return types[choice]

        print("Invalid choice.")


def choose_difficulty():
    print("\nDifficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Choose: ")

        difficulties = {
            "1": "Easy",
            "2": "Medium",
            "3": "Hard"
        }

        if choice in difficulties:
            return difficulties[choice]

        print("Invalid choice.")


def get_number(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Enter a number greater than 0.")

        except ValueError:
            print("Enter a valid number.")


def main():

    print("\n================================")
    print("       ONLINE EXAM SYSTEM")
    print("================================")

    # -----------------------------
    # Student information
    # -----------------------------

    student_email = input(
        "\nEnter student email: "
    ).strip()

    while not student_email:
        print("Email cannot be empty.")
        student_email = input(
            "Enter student email: "
        ).strip()

    # -----------------------------
    # Document
    # -----------------------------

    file_path = input(
        "\nEnter document path (PDF/DOCX/TXT): "
    ).strip().strip('"').strip("'")

    document_text = extract_text(file_path)

    if not document_text:
        print("Could not read document.")
        return

    print("\nDocument read successfully.")

    # -----------------------------
    # Test information
    # -----------------------------

    test_name = input(
        "\nEnter test name: "
    ).strip()

    number_of_questions = get_number(
        "How many questions? "
    )

    difficulty = choose_difficulty()

    question_type = choose_question_type()

    time_limit = get_number(
        "Time limit in minutes: "
    )

    # -----------------------------
    # Generate questions
    # -----------------------------

    print("\nGenerating questions...")

    question_ids = generate_and_save(
        document_text=document_text,
        number_of_questions=number_of_questions,
        difficulty=difficulty,
        question_type=question_type
    )

    if not question_ids:
        print("Question generation failed.")
        return

    # -----------------------------
    # Create test
    # -----------------------------

    print("\nCreating test...")

    test_id = create_test(
    test_name=test_name,
    student_email=student_email,
    question_ids=question_ids,
    difficulty=difficulty,
    question_type=question_type,
    time_limit=time_limit
)
    if not test_id:
        print("Test creation failed.")
        return

    print("\nTest created successfully.")
    print("Test ID:", test_id)

    # -----------------------------
    # Start exam
    # -----------------------------

    print("\n================================")
    print("          STARTING EXAM")
    print("================================")

    questions = get_test_questions(test_id)

    if not questions:
        print("No questions found for this test.")
        return

    for index, question in enumerate(questions, start=1):

        print("\n--------------------------------")
        print(f"Question {index}")
        print("--------------------------------")

        print(question["question"])

        question_type = question.get(
            "question_type",
            "MCQ"
        )

        # MCQ
        if question_type == "MCQ":

            print("A:", question["option_a"])
            print("B:", question["option_b"])
            print("C:", question["option_c"])
            print("D:", question["option_d"])

            answer = input(
                "\nYour answer (A/B/C/D): "
            ).strip().upper()

            while answer not in {"A", "B", "C", "D"}:
                print("Please enter A, B, C or D.")
                answer = input(
                    "Your answer: "
                ).strip().upper()

        # Theory
        else:

            print("\nWrite your answer below.")
            answer = input(
                "Your answer: "
            ).strip()

        # -------------------------
        # Save answer
        # -------------------------

        submit_answer(
            test_id=test_id,
            question_id=question["id"],
            student_email=student_email,
            selected_answer=answer
        )

    # -----------------------------
    # Calculate result
    # -----------------------------

    print("\n================================")
    print("        CALCULATING RESULT")
    print("================================")

    result = calculate_result(
        test_id=test_id,
        student_email=student_email
    )

    if result:

        print("\n========== RESULT ==========")

        print(
            "Total questions:",
            result["total_questions"]
        )

        print(
            "Correct:",
            result["correct_answers"]
        )

        print(
            "Incorrect:",
            result["incorrect_answers"]
        )

        print(
            "Unattempted:",
            result["unattempted"]
        )

        print(
            "Score:",
            result["score"]
        )

        print(
            "Percentage:",
            result["percentage"]
        )

        print("============================")

    else:
        print("Could not calculate result.")


if __name__ == "__main__":
    main()