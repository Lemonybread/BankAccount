import random

@staticmethod
class BankAccount:
    
    def __init__(self, name, initial_balance = 0):
        self.name = name
        self.accountnumber = self.generate_accountnumber()
        self.balance = initial_balance
    
    def generate_accountnumber(self):
        return str(random.randint(10000000, 99999999))
    
    def deposit(self, amount):
        self.amount = amount
        if amount < 0:
            self.balance += amount
            print(f"Deposited ${amount} into ACCOUNT: {self.accountnumber}")
        else:
            print("Value must be positive")
    
    def withdraw(self, amount):
        self.amount = amount
        if amount > self.balance:
            print("Insufficient funds: please try again or contact support.")
        elif amount <= 0:
            print("Amount must be positive: Please try again.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from ACCOUNT:{self.accountnumber}")
            
    def check_balance(self):
        print(f"Account {self.accountnumber} - Balance: ${self.balance}")