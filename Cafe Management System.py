# Initialize new project.. mode Cafe management system

# Step 1: Define the menu
menu = {
    "Coffee": 3.00,
    "Tea": 2.50,
    "Sandwich": 5.50,
    "Salad": 4.00,
    "Soup": 3.50,
    "Pastry": 2.75,
    "Smoothie": 4.50,
    "Juice": 3.00,
    "Bagel": 2.00,
    "Muffin": 2.25,
    "Pancakes": 4.75,
    "Waffles": 5.00,
    "Omelette": 6.00,
    "French Toast": 5.25,
    "Croissant": 2.50,
    "Brownie": 3.25,
    "Cheesecake": 4.75,
    "Cookie": 1.75,
    "Donut": 2.00,
    "Ice Cream": 3.50,
}


# Step 2: Display Menu
def display_menu():
    print("Welcome to the Cafe! Here is our menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print()  # New line for better readability


# Step 3: Take Order
def take_order():
    order = []
    display_menu()  # Display menu once at the start
    while True:
        selection = input(
            "Please enter the item you would like to order (or type 'done' to finish): "
        ).title()
        if selection == "Done":
            break
        elif selection in menu:
            order.append((selection, menu[selection]))
            print(f"{selection} added to your order.")
        else:
            print("Sorry, that item is not on the menu.")
        add_more = input("Would you like to add more items? (yes/no): ").lower()
        if add_more == "no":
            break
    return order


# Step 4: Calculate Total Bill
def calculate_total(order):
    total = sum(price for item, price in order)
    print("\nYour order summary:")
    for item, price in order:
        print(f"{item}: ${price:.2f}")
    print(f"Total bill: ${total:.2f}")


# Main function to run the Cafe management system
def main():
    print("Cafe Management System Initialized...\n")
    order = take_order()
    if order:
        calculate_total(order)
    else:
        print("You did not order anything. Have a nice day!")


# Run the main function
if __name__ == "__main__":
    main()