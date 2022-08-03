from classes import *
from login import *
from create_account import *

def Home_Screen(user):
    logged = True
    print("")
    print("Welcome Back")
    print(user.user_name)
    while logged:
        user_desicion = input("To Show Balance PRESS 'B'\nTo Deposit PRESS 'D'\nTo Withdraw PRESS 'W'\nTo Transfer Money PRESS 'T'\nPress 'Q' to Exit\n: ").upper()
        
        if user_desicion == "B":
            print(f"Your Account Balance Is: {user.account_bal}")
            print(" ")
        elif user_desicion == "D":
            user.Deposit(float(input("Enter Deposit Amount: ")))
            print(" ")
        elif user_desicion == "W":
            user.Withdraw(float(input("Enter Withdrawl Amount: ")))
            print(" ")
        elif user_desicion == "T":
            transfer_to = input("Enter Account Holder Username To Transfer To: ").upper()
            while transfer_to not in Account.Account_Database:
                print("NO User Found!")
                transfer_to = input("Enter New Username:  ").upper()

            transfer_amount = float(input("Enter Transfer Amount: "))
            print(f"Youn Sent ${Account.Transfer(user,Account.Account_Database[transfer_to],transfer_amount)} to user {transfer_to}")
            print(f"Your New Account Balance Is: {user.account_bal}")
            print(" ")
        elif user_desicion == "Q":
            Enter_Screen()
        else:
            print("Invalid Response!")
            print(" ")



def Enter_Screen(): 
    logging = True

    while logging:
        user_desiscion = input("Welcome to Jamm Bank!\nFor Login, PRESS 'L'\nFor New User Press 'N'\nTo Exit Program PRESS 'Q'\n: ").upper()

        if user_desiscion == "L":
            user_name = input("Enter Username: ").upper()
            user_pin = input("Enter Pin: ")
            Home_Screen(Login(user_name, user_pin))
            logging = False
        elif user_desiscion == "N":
            user = New_User()
            print("Returning To Main Page")
            print(" ")
        elif user_desiscion == "Q":
            quit()
        else:
            print("Invalid Response!")
            user_desiscion= input("Please Enter 'L' to Login or 'N' for New Useres.\n").upper()

Enter_Screen()
#TODO inprove readability of UI elements