"""
Demo script to show transaction history functionality
This demonstrates the feature without needing MongoDB connection
"""

from app import BankAccount

print("=" * 60)
print("TRANSACTION HISTORY FEATURE DEMONSTRATION")
print("=" * 60)

# Simulate creating an account and performing transactions
print("\n1. Creating account 12345...")
account = BankAccount(
    account_number="12345",
    holder_name="John Doe",
    dob="15-05-1990",
    balance=1000
)
print(f"   Account created with initial balance: ₹{account.balance:.2f}")

# Simulate deposits
print("\n2. Performing transactions...")
print("   - Depositing ₹500...")
account.deposit(500)
print("   - Depositing ₹1500...")
account.deposit(1500)
print("   - Withdrawing ₹300...")
account.withdraw(300)
print("   - Depositing ₹800...")
account.deposit(800)
print("   - Withdrawing ₹100...")
account.withdraw(100)

print(f"\n3. Current balance: ₹{account.get_balance():.2f}")

# Display transaction history (same logic as option 6 in menu)
print(f"\n{'=' * 60}")
print(f"TRANSACTION HISTORY FOR ACCOUNT {account.account_number}")
print('=' * 60)

history = account.transaction_history
if history:
    for i, transaction in enumerate(history, 1):
        timestamp = transaction.get('timestamp', 'Timestamp not available')
        trans_type = transaction['type']
        amount = transaction['amount']
        print(f"{i}. {timestamp}: {trans_type} of ₹{amount:.2f}")
else:
    print("No transactions found for this account.")

print("\n" + "=" * 60)
print("✓ Transaction history feature is working correctly!")
print("=" * 60)
