# max_value_ternary.py

# Prompt the user to enter three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Find the maximum value using nested ternary operators
max_value = a if (a > b and a > c) else (b if b > c else c)

# Print the maximum value
print("The maximum value is:", max_value)
