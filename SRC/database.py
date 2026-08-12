
import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from tabulate import tabulate


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
'''

@function name : print_database
@Input param   : give a table name 
@outpunt       : None 
@Description   : Its give our database table name 
                 it print that format 
                 
'''

def print_database(table_name):

    try:        

        if db is None:
            print("Database connection failed.")
            return

        cursor.execute(f"DESCRIBE {table_name}")
        columns = [column[0] for column in cursor.fetchall()]
        
       
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        print(f"\nTable: {table_name}")
        print(tabulate(rows, headers=columns, tablefmt="grid"))

    except Exception as error:
        print(f"Failed to read data from MySQL table: {error}")

    finally:
     if 'connection' in locals() and db:
        cursor.close()
        db.close()
        print("\nMySQL connection closed.")
