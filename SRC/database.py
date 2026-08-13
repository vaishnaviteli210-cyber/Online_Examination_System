
import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

def get_connection_db():
   

    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            use_pure=True
        )

        return connection

    except Error as e:
        print(f"Database Connection Error: {e}")
        return None


db = get_connection_db()
cursor = db.cursor()

