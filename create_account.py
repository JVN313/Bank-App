from classes import *

def New_User(user):
    f_name = input("First Name: ").upper()
    l_name = input("Last Name: ").upper()
    user_name = input("Username: ").upper()
    pin= input("Enter 4 Character Pin: ")

    user = Account(f_name,l_name,user_name,pin)
    return user
