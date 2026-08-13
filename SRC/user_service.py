from database import get_connection_db
import re

db = get_connection_db()
cursor = db.cursor()

#--------------email validation------------------

def email():
  while True:

    email = input("Enter Gmail Address : ")
    
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            
    if re.match(pattern, email):
        return email

#--------------phone number validation------------------

def number():
  
  try:
    while True:

       number = int(input("Enter Phone Number : "))

       if(len(str(abs(number))) == 10):
            return number
       
  except Exception as e:
      print("Please Enter Valid Number")

#--------------store data in database table------------------

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

#------------------Register----------------

def register():

  while True:

    print("\n========== REGISTER ==========")

    em = email()
    

    login_password = input("Create Login Password : ")

    smtp_password = input("Enter Gmail App Password : ")

    num = number()

    roll = input("Enter your role (Student/Teacher):").lower()

    if check_database(em,login_password):
        print("Its alredy exists")

    else:
        store_of_all(em,login_password,num,roll)
        break

# ---------------- login ----------------

def login():

    attempts = 3

    while attempts > 0:

        
        print("\n========== LOGIN ==========")

        em = email()

        login_password = input("Password : ")

        stop = input("Do You Want To Stop(s):").lower()

        if stop == "s":
            break

        attempts -= 1

        print("Invalid Email or Password.")

        if attempts > 0:

            print("Attempts Left :", attempts)

        print("\nToo many failed attempts.")

    if check_database(em,login_password):
        print("LOGIN SUCCESSFULLY")


#------------logout------------

def logout():

   while True: 

    em = email()

    list_em = []

    list_em.append(em)

    login_password = input("Password : ")

    if check_database(em,login_password):
        delete_query = "DELETE FROM member WHERE email = %s"
    
        cursor.execute(delete_query, (list_em))
        db.commit()

        if cursor.rowcount > 0:
           break
        else:
            print("No record found with that email address.")


# ---------------- login menu ----------------

def login_menu():

        print("\n===================================")
        print(" EMAIL AUTOMATION LOGIN ")
        print("===================================")
        print("1. Login")
        print("2. Register")
        print("3. logout")
        print("4. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            login()

        elif choice == "2":
            register()

        elif choice == "3":
            logout()

        elif choice == "4":
            return 

        else:
            print("Invalid Choice.")



login_menu()
db.close()
cursor.close()