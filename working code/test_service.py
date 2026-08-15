from database import get_connection_db


def create_test(
    test_name,
    student_email,
    question_ids,
    difficulty,
    question_type="MCQ",
    time_limit=None
):
    db = get_connection_db()

    if db is None:
        print("Database connection failed.")
        return None

    cursor = db.cursor()

    try:
        # Check that we have enough generated questions
        number_of_questions = len(question_ids)

        if number_of_questions == 0:
            print("No questions were provided.")
            return None

        # Step 1: Create test
        query = """
            INSERT INTO tests (
                test_name,
                student_email,
                number_of_questions,
                difficulty,
                question_type,
                time_limit
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                test_name,
                student_email,
                number_of_questions,
                difficulty,
                question_type,
                time_limit
            )
        )

        test_id = cursor.lastrowid

        # Step 2: Add the EXACT generated questions
        insert_question = """
            INSERT INTO test_questions (
                test_id,
                question_id,
                question_order
            )
            VALUES (%s, %s, %s)
        """

        for order, question_id in enumerate(question_ids, start=1):

            cursor.execute(
                insert_question,
                (
                    test_id,
                    question_id,
                    order
                )
            )

        db.commit()

        print("Test created successfully.")
        print("Test ID:", test_id)
        print("Questions added:", question_ids)

        return test_id

    except Exception as e:

        db.rollback()

        print(f"Test creation error: {e}")

        return None

    finally:

        cursor.close()
        db.close()