# Take input from the user
n = int(input("Enter the number of rows: "))

# Print statement before the pattern
print("Starting the Right-Angled Triangle pattern:")

# Loop through each row
for i in range(1, n + 1):
    # Loop to print numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")
    # Print a newline after each row
    print()

# Print statement after the pattern
print("Pattern completed.")
