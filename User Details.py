def get_user_details():
    # Read user details
    name = input("Enter your name: ")
    contact_number = input("Enter your contact number: ")
    email = input("Enter your email: ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

    # Print user details
    print("\nUser Details:")
    print(f"Name: {name}")
    print(f"Contact Number: {contact_number}")
    print(f"Email: {email}")
    print(f"Birthdate: {birthdate}")


if __name__ == "__main__":
    get_user_details()
