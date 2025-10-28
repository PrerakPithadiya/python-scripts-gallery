from database import Database
from datetime import datetime
import sys

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
        self.transaction_history.append({"type": transaction_type, "amount": amount, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

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

    def transfer_funds(self, from_account_number, to_account_number, amount):
        # Get both accounts
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if not from_account or not to_account:
            return False, "One or both accounts not found."
        if from_account.get_balance() < amount or amount <= 0:
            return False, "Insufficient funds or invalid amount."
        # Update balances
        from_account.balance -= amount
        to_account.balance += amount
        from_account.add_transaction("Transfer Out", amount)
        to_account.add_transaction("Transfer In", amount)
        self.update_account(from_account)
        self.update_account(to_account)
        # Also update in DB transaction collection
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        self.db.add_transaction(from_account_number, "Transfer Out", amount, date, time)
        self.db.add_transaction(to_account_number, "Transfer In", amount, date, time)
        return True, "Transfer successful."

def do_create_account(bank):
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

def do_deposit(bank):
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

def do_withdraw(bank):
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

def do_account_details(bank):
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

def do_delete_account(bank):
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

def do_view_transaction_history(bank):
    account_number = input("Enter your account number: ")
    account = bank.get_account(account_number)
    if account:
        print(f"\n==== Transaction History for Account {account_number} ====")
        history = account.transaction_history
        if history:
            for transaction in history:
                print(f"  - {transaction['timestamp']}: {transaction['type']} of ₹{transaction['amount']:.2f}")
        else:
            print("No transactions found for this account.")
    else:
        print("Invalid account number.")

def do_transfer_funds(bank):
    from_account_number = input("Enter your account number: ")
    to_account_number = input("Enter recipient's account number: ")
    amount_str = input("Enter amount to transfer: ₹")
    if amount_str.replace('.', '', 1).isdigit():
        amount = float(amount_str)
        success, message = bank.transfer_funds(from_account_number, to_account_number, amount)
        print(message)
    else:
        print("Invalid amount. Please enter a number.")

def main():
    try:
        from config import MONGO_CONNECTION_STRING
    except ImportError:
        print("Error: Configuration file 'config.py' not found.")
        print("Please create it by copying 'config_example.py' and adding your MongoDB connection string.")
        sys.exit(1)

    bank = Bank(MONGO_CONNECTION_STRING)

    while True:
        print("\n==== Bank Menu ====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Account Details")
        print("5. Delete Account")
        print("6. View Transaction History")
        print("7. Transfer Funds")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            do_create_account(bank)
        elif choice == "2":
            do_deposit(bank)
        elif choice == "3":
            do_withdraw(bank)
        elif choice == "4":
            do_account_details(bank)
        elif choice == "5":
            do_delete_account(bank)
        elif choice == "6":
            do_view_transaction_history(bank)
        elif choice == "7":
            do_transfer_funds(bank)
        elif choice == "8":
            print("Thank you for using the bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()