from database import get_connection_db

db = get_connection_db()
cursor = db.cursor()


def store_of_all(email, login_pass,num,roll):
    try:
        if db is None:
            print("Database connection failed.")
            return

        cursor.execute(
            """
            INSERT INTO member( email, login_pass, num, roll)
            VALUES( %s, %s, %s, %s)
            """,
            ( email, login_pass, num, roll)
        )

        print("store successfully")

        if( roll == "student"):

            cursor.execute(
                """
                INSERT INTO student( email, login_pass, num, roll)
                VALUES( %s, %s, %s, %s)
                """,
                ( email, login_pass, num, roll)
            )
            
        elif( roll == "teacher"):
            cursor.execute(
                """
                INSERT INTO teacher( email, login_pass, num, roll)
                VALUES( %s, %s, %s, %s)
                """,
                ( email, login_pass, num, roll)
            )

        db.commit()
            
    except Exception as e:
    
        if db:
          print(f"Database error occurred: {e}. Transaction rolled back.")

    finally:
        if db and db.is_connected():
            print("Database connection safely closed.")

#--------------check the data is avaliable in table------------------

def check_database(em,num):

    input_one = em
    input_two = num


    query = "SELECT 1 FROM member WHERE email = %s AND login_pass = %s LIMIT 1"

    cursor.execute(query, (input_one, input_two))

    if cursor.fetchone():
       return True
    else:
       return False

'''
#--------------print database table------------------

def print_database():

  try:
    cursor.execute("SHOW TABLES;")
    tables = [t[0] for t in cursor.fetchall()]
    
    for table in tables:
        print(f"\n====== {table} =======")
        cursor.execute(f"SELECT * FROM `{table}`")
        for row in cursor.fetchall():
            print(row)
                
  except Exception as e:
    print(f"Error: {e}")    

'''