from database import Database
from datetime import datetime

class BankAccount:
    def __init__(self, account_number, holder_name, dob, balance=0, transaction_history=None):
        self.account_number = account_number
        self.holder_name = holder_name
        self.dob = dob
        self.balance = balance
        self.transaction_history = transaction_history if transaction_history is not None else []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.add_transaction("Withdrawal", amount)
            return True
        return False

    def get_balance(self):
        return self.balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "holder_name": self.holder_name,
            "dob": self.dob,
            "balance": self.balance,
            "transaction_history": self.transaction_history
        }

    def add_transaction(self, transaction_type, amount):
        self.transaction_history.append({"type": transaction_type, "amount": amount})

class Bank:
    def __init__(self, connection_string):
        self.db = Database(connection_string)

    def create_account(self, account_number, holder_name, dob, initial_deposit):
        if self.db.get_account(account_number):
            return None  # Account number already exists
        
        new_account = BankAccount(account_number, holder_name, dob, initial_deposit)
        self.db.create_account(new_account.to_dict())
        return new_account

    def get_account(self, account_number):
        account_data = self.db.get_account(account_number)
        if account_data:
            account_data.pop('_id', None)
            return BankAccount(**account_data)
        return None

    def update_account(self, account):
        self.db.update_account(account.account_number, account.to_dict())

    def delete_account(self, account_number):
        account = self.get_account(account_number)
        if account and account.get_balance() == 0:
            self.db.delete_account(account_number)
            return True
        return False

def main():
    connection_string = "mongodb+srv://prerakpithadiya_db_user:SV7OaGSBN0LcKcJY@cluster0.s2lpezb.mongodb.net/"
    bank = Bank(connection_string)

    while True:
        print("\n==== Bank Menu ====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Account Details")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            holder_name = input("Enter account holder name: ")
            account_number = input("Enter desired account number: ")
            
            while True:
                dob_str = input("Enter date of birth (DD-MM-YYYY): ")
                try:
                    # Validate and standardize the date format
                    dob = datetime.strptime(dob_str, "%d-%m-%Y").strftime("%d-%m-%Y")
                    break
                except ValueError:
                    print("Invalid date format. Please use DD-MM-YYYY.")

            initial_deposit = 0
            while initial_deposit < 1000:
                initial_deposit_str = input("Enter initial deposit amount (minimum ₹1000): ₹")
                if initial_deposit_str.replace('.', '', 1).isdigit():
                    initial_deposit = float(initial_deposit_str)
                    if initial_deposit < 1000:
                        print("Initial deposit must be at least ₹1000. Please try again.")
                else:
                    print("Invalid amount. Please enter a number.")

            if bank.get_account(account_number):
                print("Account number already exists. Please choose a different one.")
            else:
                bank.create_account(account_number, holder_name, dob, initial_deposit)
                print("Account created successfully!")

        elif choice == "2":
            account_number = input("Enter your account number: ")
            account = bank.get_account(account_number)
            if account:
                amount_str = input("Enter the amount to deposit: ₹")
                if amount_str.replace('.', '', 1).isdigit():
                    amount = float(amount_str)
                    if account.deposit(amount):
                        bank.update_account(account)
                        print(f"Deposit successful. Your new balance is: ₹{account.get_balance():.2f}")
                    else:
                        print("Invalid deposit amount.")
                else:
                    print("Invalid amount. Please enter a number.")
            else:
                print("Invalid account number.")

        elif choice == "3":
            account_number = input("Enter your account number: ")
            account = bank.get_account(account_number)
            if account:
                current_balance = account.get_balance()
                print(f"Your current balance is: ₹{current_balance:.2f}")

                if current_balance == 0:
                    print("You cannot withdraw from an account with a zero balance.")
                else:
                    while True:
                        amount_str = input("Enter the amount to withdraw: ₹")
                        if amount_str.replace('.', '', 1).isdigit():
                            amount = float(amount_str)
                            if account.withdraw(amount):
                                bank.update_account(account)
                                print(f"Withdrawal successful. Your new balance is: ₹{account.get_balance():.2f}")
                                break
                            else:
                                print("Invalid withdrawal amount or insufficient funds. Please enter a valid amount.")
                        else:
                            print("Invalid amount. Please enter a number.")
            else:
                print("Invalid account number.")

        elif choice == "4":
            account_number = input("Enter your account number: ")
            account = bank.get_account(account_number)
            if account:
                details = account.to_dict()
                print("\n==== Account Details ====")
                print(f"Account Holder Name: {details['holder_name']}")
                print(f"Account Number: {details['account_number']}")
                print(f"Date of Birth: {details['dob']}")
                print(f"Balance: ₹{details['balance']:.2f}")
            else:
                print("Invalid account number.")

        elif choice == "5":
            account_number = input("Enter the account number to delete: ")
            account = bank.get_account(account_number)
            if account:
                if account.get_balance() == 0:
                    holder_name_confirm = input("For verification, please enter the account holder's name: ")
                    dob_confirm_str = input("For verification, please enter the account holder's date of birth (DD-MM-YYYY): ")

                    try:
                        # Compare dates by parsing them into datetime objects
                        dob_confirm_date = datetime.strptime(dob_confirm_str, "%d-%m-%Y").date()
                        stored_dob_date = datetime.strptime(account.dob, "%d-%m-%Y").date()

                        if holder_name_confirm == account.holder_name and dob_confirm_date == stored_dob_date:
                            confirm = input("Are you sure you want to delete this account? (yes/no): ").lower()
                            if confirm == 'yes':
                                if bank.delete_account(account_number):
                                    print("Account deleted successfully.")
                                else:
                                    print("Error deleting account.")
                            else:
                                print("Account deletion cancelled.")
                        else:
                            print("Verification failed. Account deletion cancelled.")
                    except ValueError:
                        print("Invalid date format. Please use DD-MM-YYYY. Account deletion cancelled.")
                else:
                    print("Account must be empty before it can be deleted. Please withdraw all funds.")
            else:
                print("Invalid account number.")

        elif choice == "6":
            print("Thank you for using the bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()