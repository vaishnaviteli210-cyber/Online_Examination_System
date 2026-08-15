from database import get_connection_db


def submit_answer(
    test_id,
    question_id,
    student_email,
    selected_answer
):
    db = get_connection_db()

    if db is None:
        print("Database connection failed.")
        return False

    cursor = db.cursor()

    try:
        # Get the correct answer
        cursor.execute(
            """
            SELECT correct_answer
            FROM questions
            WHERE id = %s
            """,
            (question_id,)
        )

        question = cursor.fetchone()

        if question is None:
            print("Question not found.")
            return False

        correct_answer = question[0].upper()
        selected_answer = selected_answer.upper()

        # Check answer
        is_correct = selected_answer == correct_answer

        # Save student's answer
        cursor.execute(
            """
            INSERT INTO student_answers (
                test_id,
                question_id,
                student_email,
                selected_answer,
                is_correct
            )
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                test_id,
                question_id,
                student_email,
                selected_answer,
                is_correct
            )
        )

        db.commit()

        print("Answer submitted successfully.")

        if is_correct:
            print("Answer is correct.")
        else:
            print("Answer is incorrect.")

        return True

    except Exception as e:
        db.rollback()
        print(f"Answer submission error: {e}")
        return False

    finally:
        cursor.close()
        db.close()