import re

from database import get_connection_db
from user_repositry import store_of_all, check_database

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