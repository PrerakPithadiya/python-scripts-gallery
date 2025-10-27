from app import BankAccount

# Create a mock account with transaction history
account = BankAccount(
    account_number="12345",
    holder_name="Test User",
    dob="01-01-1990",
    balance=5000
)

# Add some transactions
account.add_transaction("Deposit", 1000)
account.add_transaction("Withdrawal", 500)
account.add_transaction("Deposit", 2000)

# Display transaction history (simulating option 6 logic)
print(f"\n==== Transaction History for Account {account.account_number} ====")
history = account.transaction_history
if history:
    for transaction in history:
        timestamp = transaction.get('timestamp', 'Timestamp not available')
        print(f"  - {timestamp}: {transaction['type']} of ₹{transaction['amount']:.2f}")
else:
    print("No transactions found for this account.")
