from pymongo import MongoClient

# MongoDB connection setup
def get_database():
    # Replace the connection string with your MongoDB URI
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['users']  # Connect to the 'users' database

def get_collection():
    db = get_database()
    return db['registration_system']  # Use a different collection for registration

def insert_user(user_data):
    """Insert a new user with additional registration data."""
    collection = get_collection()
    result = collection.insert_one(user_data)
    return result.inserted_id

def check_existing_user(username, email):
    """Check if username or email already exists."""
    collection = get_collection()
    return collection.find_one({
        "$or": [
            {"username": username},
            {"email": email}
        ]
    })
