from pymongo import MongoClient

# MongoDB connection setup
def get_database():
    # Replace the connection string with your MongoDB URI
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['users']  # Connect to the 'users' database

def get_collection():
    db = get_database()
    return db['login_system']  # Connect to the 'login_system' collection

def insert_user(user):
    collection = get_collection()
    result = collection.insert_one(user)
    print(f"Inserted ID: {result.inserted_id}")
