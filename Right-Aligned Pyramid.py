# Get the number of rows from the user
n = int(input("Enter the number of rows: "))

# Print a message before the pattern is printed
print("Printing the pattern:")

# Loop through each row
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print stars with spaces
    for j in range(i):
        print("* ", end="")

    # Move to the next line
    print()

# Print a message after the pattern is printed
print("Pattern printed successfully!")
