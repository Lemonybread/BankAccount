from Bank import Bank

@staticmethod
class BankSystem:
    def __init__(self):
        self.bank = Bank()
        
    def show_menu(self):
         while True:
            print("\nBank Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                print("Exiting the banking system. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
                
    def create_account(self):
        name = input("Enter the account holder's name: ")
        initial_deposit = float(input("Enter the initial deposit amount: "))
        self.bank.create_account(name, initial_deposit)

    def deposit(self):
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to deposit: "))
        self.bank.deposit_to_account(account_number, amount)

    def withdraw(self):
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to withdraw: "))
        self.bank.withdraw_from_account(account_number, amount)

    def check_balance(self):
        account_number = input("Enter the account number: ")
        self.bank.check_account_balance(account_number)
