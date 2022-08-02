import random

class Account:

    Account_Database ={}

    def Account_Num_Creator(self):
        Account_Num_List = []
        new_num = random.randint(1000,2000)
        while new_num in Account_Num_List:
            new_num = random.randint(1000,2000)
        
        Account_Num_List.append(new_num)
        return Account_Num_List[len(Account_Num_List)-1]
        

    def __init__(self,f_name,l_name, user_name, pin):
        self.f_name = f_name
        self.l_name = l_name
        self.user_name = user_name

        while len(pin) != 4:
            print("Selected PIN must contain 4 characters")
            pin = input("Please Enter A New Pin:  ") 
        
        self.pin = pin
        self.account_num = self.Account_Num_Creator()
        self.account_bal = 0

        Account.Account_Database.update({self.user_name:self})

    def __repr__(self) -> str:
        return f"{self.f_name},{self.l_name[0]}/ Account Number/{self.account_num} Account Balance/{self.account_bal}"

    def Deposit(self, amount):
        self.account_bal = self.account_bal + amount
        print(f"Your Acccount Balance is {self.account_bal}")

    def Withdraw(self, amount):
        while amount > self.account_bal:
            print(f"You Tried To Withdraw {amount}, Which Exceeds Your Account Balance Of {self.account_bal}. Please Choose A New Amount.")
            amount = float(input("Enter New Amount: "))

        self.account_bal = self.account_bal - amount

        print(f"Your Acccount Balance is {self.account_bal}")

    @classmethod
    def Transfer(cls,account1,account2,amount):
        account1.Withdraw(amount)
        account2.account_bal = account2.account_bal + amount

