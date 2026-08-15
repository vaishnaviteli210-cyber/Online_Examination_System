from database import get_connection_db
from question_validator import validate_question


def save_question(question_data):

    # 1. Validate question
    valid, message = validate_question(question_data)

    if not valid:
        print(f"Question validation failed: {message}")
        return None

    # 2. Connect to database
    db = get_connection_db()

    if db is None:
        print("Database connection failed.")
        return None

    cursor = db.cursor()

    try:

        question_type = question_data.get(
            "question_type",
            "MCQ"
        )

        # -------------------------
        # MCQ
        # -------------------------
        if question_type == "MCQ":

            query = """
                INSERT INTO questions (
                    question,
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    correct_answer,
                    explanation,
                    difficulty,
                    question_type,
                    theory_answer
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                question_data["question"],
                question_data["option_a"],
                question_data["option_b"],
                question_data["option_c"],
                question_data["option_d"],
                question_data["correct_answer"].upper(),
                question_data.get("explanation"),
                question_data["difficulty"].capitalize(),
                "MCQ",
                None
            )

        # -------------------------
        # Theory
        # -------------------------
        elif question_type == "Theory":

            query = """
                INSERT INTO questions (
                    question,
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    correct_answer,
                    explanation,
                    difficulty,
                    question_type,
                    theory_answer
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                question_data["question"],
                None,
                None,
                None,
                None,
                None,
                question_data.get("explanation"),
                question_data["difficulty"].capitalize(),
                "Theory",
                question_data["theory_answer"]
            )

        cursor.execute(query, values)

        db.commit()

        question_id = cursor.lastrowid

        print("Question saved successfully.")
        print("Question ID:", question_id)

        return question_id

    except Exception as e:

        db.rollback()

        print(f"Database error: {e}")

        return None

    finally:

        cursor.close()
        db.close()