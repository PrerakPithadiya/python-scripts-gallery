from db import get_collection, check_existing_user, insert_user
from auth import hash_password, validate_password, validate_email
from datetime import datetime, timezone

def get_user_input(prompt, validator=None):
    """Get and validate user input."""
    while True:
        value = input(prompt).strip()
        if validator:
            is_valid, message = validator(value)
            if not is_valid:
                print(f"Error: {message}")
                continue
        return value

def register_user():
    """Register a new user with detailed information."""
    print("\n=== User Registration ===")
    
    # Get username
    while True:
        username = input("Enter username: ").strip()
        if len(username) < 3:
            print("Username must be at least 3 characters long")
            continue
        break

    # Get email
    email = get_user_input("Enter email: ", validate_email)

    # Check if username or email already exists
    if check_existing_user(username, email):
        print("Username or email already exists! Please try different credentials.")
        return

    # Get and validate password
    while True:
        password = input("Enter password: ")
        is_valid, message = validate_password(password)
        if not is_valid:
            print(f"Error: {message}")
            continue
        
        confirm_password = input("Confirm password: ")
        if password != confirm_password:
            print("Passwords do not match!")
            continue
        break

    # Get additional information
    full_name = input("Enter full name: ").strip()
    while True:
        birth_date = input("Enter birth date (DD-MM-YYYY): ").strip()
        try:
            # Convert birth_date string to datetime object
            birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format! Please use DD-MM-YYYY")

    # Create user document
    user_data = {
        "username": username,
        "email": email,
        "password": hash_password(password),
        "full_name": full_name,
        "birth_date": birth_date.strftime("%d-%m-%Y"),
        "registration_date": datetime.now(timezone.utc).strftime("%d-%m-%Y"),
        "last_updated": datetime.now(timezone.utc).strftime("%d-%m-%Y")
    }

    # Insert user into database
    try:
        user_id = insert_user(user_data) 
        print("\nRegistration successful!")
        print(f"User ID: {user_id}")
    except Exception as e:
        print(f"Error during registration: {str(e)}")

def main():
    while True:
        print("\n=== Registration System ===")
        print("1. Register New User")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            print("Thank you for using the registration system!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()