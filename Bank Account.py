# Write a python program to ATM & Mad libs game project


class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def display_menu(self):
        print("\n==== ATM Menu ====")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Quit")

    def check_balance(self):
        print(f"Your balance is ${self.balance}")

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. Updated balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")


def main():
    atm = ATM()

    while True:
        atm.display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw_cash(amount)
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit_cash(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
