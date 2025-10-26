
import pymongo

class Database:
    def __init__(self, connection_string, db_name="bank_system", collection_name="accounts"):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_account(self, account_data):
        self.collection.insert_one(account_data)

    def get_account(self, account_number):
        return self.collection.find_one({"account_number": account_number})

    def update_account(self, account_number, updated_data):
        self.collection.update_one({"account_number": account_number}, {"$set": updated_data})

    def delete_account(self, account_number):
        self.collection.delete_one({"account_number": account_number})
