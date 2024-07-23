import itertools


def main():
    # Prompt the user to enter 10 integers
    numbers = []
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter integer {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Generate all combinations of picking two numbers
    combinations = list(itertools.combinations(numbers, 2))

    # Display the combinations
    print("All combinations of picking two numbers from the entered integers:")
    for combo in combinations:
        print(combo)


if __name__ == "__main__":
    main()
