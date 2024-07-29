def count_digit_occurrences(input_string):
    # Initialize a dictionary to store the count of each digit
    digit_count = {str(i): 0 for i in range(10)}

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            # Increment the count of the digit in the dictionary
            digit_count[char] += 1

    # Print the counts of each digit
    for digit, count in digit_count.items():
        if count > 0:
            print(f"{digit} ({count} time{'s' if count > 1 else ''})")


# Main function to take input from the user
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    count_digit_occurrences(input_string)
