def calculate_change(quarters, dimes, nickels, pennies):
    # Define the value of each coin in dollars
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    # Calculate the total value in dollars
    total_value = (
        (quarters * quarter_value)
        + (dimes * dime_value)
        + (nickels * nickel_value)
        + (pennies * penny_value)
    )

    return total_value


# Example usage
quarters = int(input("Enter the number of quarters: "))
dimes = int(input("Enter the number of dimes: "))
nickels = int(input("Enter the number of nickels: "))
pennies = int(input("Enter the number of pennies: "))

total_dollars = calculate_change(quarters, dimes, nickels, pennies)
print(f"The total value of change is ${total_dollars:.2f}")
