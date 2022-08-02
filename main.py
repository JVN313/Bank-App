from telnetlib import PRAGMA_HEARTBEAT
from classes import *
from login import *
from create_account import *

james =''
james = New_User(james)

def Home_Screen(user):
    print("")
    print("Welcome Back")
    print(user.user_name)
    print("To Show Balance PRESS 'B'")
    print("To Deposit PRESS 'D' ")
    print("To Withdraw PRESS 'W' ")
    user_desicion = input("To Transfer Money PRESS 'T'\n: ").upper()
    if user_desicion == "B":
        print(f"Your Account Balance Is: {user.account_bal}")

def Enter_Screen():
    print("Welcome to Jamm Bank!")
    print("For Login, PRESS 'L'")
    user_desiscion = input("For New User Press 'N'\n").upper()
    logging = True

    while logging:
        if user_desiscion == "L":
            user_name = input("Enter Username: ").upper()
            user_pin = input("Enter Pin: ")
            Home_Screen(Login(user_name, user_pin))
            logging = False
        elif user_desiscion == "N":
            user_name = ""
            user_name = New_User(user_name)
            logging = False
        else:
            print("Invalid Response!")
            user_desiscion= input("Please Enter 'L' to Login or 'N' for New Useres.\n").upper()

Enter_Screen()
#TODO finish creating the UI starting with the Home_Screen Function options