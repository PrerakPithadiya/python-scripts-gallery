from db import get_collection
from auth import hash_password, verify_password

def register_user():
    """Register a new user."""
    username = input("Enter username: ")
    collection = get_collection()

    # Check if username already exists
    if collection.find_one({"username": username}):
        print("Username already exists! Please choose a different username.")
        return

    password = input("Enter password: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Insert into MongoDB
    user = {"username": username, "password": hashed_password}
    result = collection.insert_one(user)
    print(f"User registered successfully! Inserted ID: {result.inserted_id}")

def login_user():
    """Log in an existing user."""
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Fetch user from MongoDB
    collection = get_collection()
    user = collection.find_one({"username": username})

    if user:
        # Verify the password
        if verify_password(password, user['password']):
            print("Login successful!")
        else:
            print("Invalid password!")
    else:
        print("User not found!")

def view_data():
    """View all registered users."""
    collection = get_collection()
    for document in collection.find():
        print(document)

def delete_user():
    """Delete a user by username."""
    username = input("Enter username to delete: ")
    collection = get_collection()

    # Delete the user
    result = collection.delete_one({"username": username})
    if result.deleted_count > 0:
        print("User deleted successfully!")
    else:
        print("User not found!")

def update_password():
    """Update a user's password by username."""
    username = input("Enter username to update password: ")
    collection = get_collection()

    # Check if user exists
    user = collection.find_one({"username": username})
    if not user:
        print("User not found!")
        return

    new_password = input("Enter new password: ")

    # Hash the new password
    hashed_password = hash_password(new_password)

    # Update the password in MongoDB
    result = collection.update_one(
        {"username": username},
        {"$set": {"password": hashed_password}}
    )

    if result.modified_count > 0:
        print("Password updated successfully!")
    else:
        print("Failed to update password!")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. View Data")
        print("4. Exit")
        print("5. Delete User")
        print("6. Update Password")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            view_data()
        elif choice == '4':
            print("Exiting...")
            break
        elif choice == '5':
            delete_user()
        elif choice == '6':
            update_password()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
