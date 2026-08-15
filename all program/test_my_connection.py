from database import get_connection_db


db = get_connection_db()

if db is None:
    print("Database connection failed.")
else:
    try:
        cursor = db.cursor()

        cursor.execute("SHOW TABLES")

        tables = cursor.fetchall()

        print("\nTables in examination database:")

        for table in tables:
            print(table[0])

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        db.close()