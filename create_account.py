from classes import *

def New_User(user):
    f_name = input("First Name")
    l_name = input("LAST name")
    user_name = input("Username")
    pin= input("Enter 4 Character Pin")

    user = Account(f_name,l_name,user_name,pin)
    return user
