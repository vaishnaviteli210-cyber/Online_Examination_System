from database import get_connection_db

db = get_connection_db()
cursor = db.cursor()


def store_of_all(file_path):

    file_p = []
    file_p.append(file_path)
    try:
        if db is None:
            print("Database connection failed.")
            return

        cursor.execute(
            """
            INSERT INTO file_path( file_path)
            VALUES( %s)
            """,
            ( file_p)
        )

        db.commit()
            
    except Exception as e:
    
        if db:
          print(f"Database error occurred: {e}. ")

    finally:
        if db and db.is_connected():
            print("Database connection safely closed.")
