def eliminate_duplicates(input_list):
    # Use a set to eliminate duplicates
    unique_values = list(set(input_list))
    return unique_values


if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter numbers separated by spaces: ")

    # Convert the input string to a list of integers
    input_list = list(map(int, user_input.split()))

    # Eliminate duplicates
    unique_list = eliminate_duplicates(input_list)

    # Display the unique values on the console
    print("Unique values:", unique_list)
