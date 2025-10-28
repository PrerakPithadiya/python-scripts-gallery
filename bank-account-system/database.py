
import pymongo
import certifi
from datetime import datetime

class Database:
    def __init__(self, connection_string, db_name="bank_system", collection_name="accounts"):
        print(f"Connecting to: {connection_string}")
        self.client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.transactions = self.db["transactions"]

    def create_account(self, account_data):
        self.collection.insert_one(account_data)

    def get_account(self, account_number):
        return self.collection.find_one({"account_number": account_number})

    def update_account(self, account_number, updated_data):
        self.collection.update_one({"account_number": account_number}, {"$set": updated_data})

    def delete_account(self, account_number):
        self.collection.delete_one({"account_number": account_number})

    def add_transaction(self, account_number, transaction_type, amount, date, time):
        transaction = {
            "account_number": account_number,
            "type": transaction_type,
            "amount": amount,
            "date": date,
            "time": time
        }
        self.transactions.insert_one(transaction)

    def get_transactions(self, account_number):
        return list(self.transactions.find({"account_number": account_number}))
