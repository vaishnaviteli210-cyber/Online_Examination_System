from database import get_connection_db


def get_test_questions(test_id):

    db = get_connection_db()

    if db is None:
        print("Database connection failed.")
        return []

    cursor = db.cursor(dictionary=True)

    try:
        query = """
            SELECT
                q.id,
                q.question,
                q.option_a,
                q.option_b,
                q.option_c,
                q.option_d,
                tq.question_order
            FROM test_questions tq
            JOIN questions q
                ON tq.question_id = q.id
            WHERE tq.test_id = %s
            ORDER BY tq.question_order
        """

        cursor.execute(query, (test_id,))

        questions = cursor.fetchall()

        return questions

    except Exception as e:
        print(f"Error loading test questions: {e}")
        return []

    finally:
        cursor.close()
        db.close()