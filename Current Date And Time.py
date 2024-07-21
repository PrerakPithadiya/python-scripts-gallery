import time
from datetime import datetime
import os


def clear_console():
    # Clear the console based on the operating system
    os.system("cls" if os.name == "nt" else "clear")


while True:
    # Clear the console
    clear_console()

    # Get the current date and time
    now = datetime.now()

    # Format the date and time
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Print the current date and time
    print("Current Date and Time: ", current_time)

    # Wait for 1 second before updating
    time.sleep(1)
