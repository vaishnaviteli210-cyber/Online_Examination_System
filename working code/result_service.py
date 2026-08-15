from database import get_connection_db


def calculate_result(test_id, student_email):

    db = get_connection_db()

    if db is None:
        print("Database connection failed.")
        return None

    cursor = db.cursor(dictionary=True)

    try:
        # Get total number of questions in the test
        cursor.execute(
            """
            SELECT COUNT(*) AS total_questions
            FROM test_questions
            WHERE test_id = %s
            """,
            (test_id,)
        )

        test_data = cursor.fetchone()
        total_questions = test_data["total_questions"]

        # Get student's submitted answers
        cursor.execute(
            """
            SELECT
                COUNT(*) AS answered,
                SUM(CASE WHEN is_correct = TRUE THEN 1 ELSE 0 END)
                    AS correct_answers
            FROM student_answers
            WHERE test_id = %s
            AND student_email = %s
            """,
            (test_id, student_email)
        )

        answer_data = cursor.fetchone()

        answered = answer_data["answered"] or 0
        correct_answers = answer_data["correct_answers"] or 0

        incorrect_answers = answered - correct_answers
        unattempted = total_questions - answered

        # Score
        score = correct_answers

        # Percentage
        if total_questions > 0:
            percentage = (correct_answers / total_questions) * 100
        else:
            percentage = 0

        # Save result
        cursor.execute(
            """
            INSERT INTO results (
                test_id,
                student_email,
                total_questions,
                correct_answers,
                incorrect_answers,
                unattempted,
                score,
                percentage
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                test_id,
                student_email,
                total_questions,
                correct_answers,
                incorrect_answers,
                unattempted,
                score,
                percentage
            )
        )

        db.commit()

        result = {
            "test_id": test_id,
            "student_email": student_email,
            "total_questions": total_questions,
            "correct_answers": correct_answers,
            "incorrect_answers": incorrect_answers,
            "unattempted": unattempted,
            "score": score,
            "percentage": round(percentage, 2)
        }

        return result

    except Exception as e:
        db.rollback()
        print(f"Result calculation error: {e}")
        return None

    finally:
        cursor.close()
        db.close()