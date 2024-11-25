from bankAccount import BankAccount


@staticmethod
class Bank:
    def __init__(self):
        self.accounts = {}
        
    def create_account(self, name, initial_deposit = 0):
        account = BankAccount(name, initial_deposit)
        self.accounts[account.accountnumber] = account
        print(f"Account created for {name}. Account Number: {account.accountnumber}")
        
    def find_accounts(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            print(f"Account with number {account_number} not found.")
            return None
        
    def deposit_to_account(self,account_number,amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"Account with number {account_number} not found.")
    
    def withdrawl_from_account(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"Account with number {account_number} not found.")
    
    def check_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.check_balance()
        else:
            print(f"Account with number {account_number} not found.")