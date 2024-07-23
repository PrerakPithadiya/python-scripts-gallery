def main():
    try:
        # Read the number of elements
        n = int(input("Enter the number of elements: "))

        # Initialize a list to store the numbers
        numbers = []

        # Read n numbers from the user
        for i in range(n):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)

        # Calculate the average
        average = sum(numbers) / n

        # Print the average without saving to a file
        print(f"The average of the entered numbers is: {average}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
