import mysql.connector
from datetime import datetime

def create_database():
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="prerak!2025_SQL*"
    )
    cursor = connection.cursor()    

    # Create a new database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS NewLoginFormDB")
    connection.close()

def create_table():
    # Connect to the newly created database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="prerak!2025_SQL*",
        database="NewLoginFormDB"
    )
    cursor = connection.cursor()

    # Create a table for storing user credentials if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            date DATE NOT NULL,
            time TIME NOT NULL
        )
    """)
    connection.close()

def store_credentials(username, password):
    # Get the current date and time
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="prerak!2025_SQL*",
        database="NewLoginFormDB"
    )
    cursor = connection.cursor()

    # Insert the credentials along with date and time into the Users table
    cursor.execute(
        "INSERT INTO Users (username, password, date, time) VALUES (%s, %s, %s, %s)",
        (username, password, current_date, current_time)
    )
    connection.commit()
    connection.close()

def main():
    create_database()
    create_table()

    # Prompt user for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Ask for confirmation to store credentials
    confirm = input("Do you want to store these credentials in the database? (yes/no): ").strip().lower()

    if confirm == "yes":
        store_credentials(username, password)
        print("Credentials have been stored in the database.")
    else:
        print("Credentials were not stored.")

if __name__ == "__main__":
    main()
