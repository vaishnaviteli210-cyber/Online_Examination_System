from database import get_connection_db


db = get_connection_db()

if db:
    print("Python → MySQL connection successful.")
    db.close()
else:
    print("Python → MySQL connection failed.")