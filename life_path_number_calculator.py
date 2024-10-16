"""
Life Path Number Calculator

This module calculates a person's Life Path Number based on their birth date.
The Life Path Number is a numerological concept that represents the path an individual
will take through life and the challenges they may face along the way.

Functions:
    reduce_to_single_digit(n: int) -> int
    calculate_life_path_number(day: int, month: int, year: int) -> int
    main() -> None

Usage:
    Run this script directly to use the interactive calculator.
    Import the calculate_life_path_number function to use in other scripts.
"""


def reduce_to_single_digit(n):
    """
    Reduce a number to a single digit or master number (11, 22, 33).

    Args:
        n (int): The number to be reduced.

    Returns:
        int: The reduced number (single digit or master number).
    """
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(digit) for digit in str(n))
    return n


def calculate_life_path_number(day, month, year):
    """
    Calculate the life path number based on the birth date.

    Args:
        day (int): The day of birth (1-31).
        month (int): The month of birth (1-12).
        year (int): The year of birth (e.g., 2000).

    Returns:
        int: The calculated Life Path Number.
    """
    # Reduce month, day, and year to single digits or master numbers
    month_reduced = reduce_to_single_digit(month)
    day_reduced = reduce_to_single_digit(day)
    year_reduced = reduce_to_single_digit(year)

    # Sum the reduced values
    life_path_sum = month_reduced + day_reduced + year_reduced

    # Reduce the total sum to a single digit or master number
    return reduce_to_single_digit(life_path_sum)


def main():
    """
    Main function to run the interactive Life Path Number Calculator.

    This function prompts the user for their birth date, calculates
    their Life Path Number, and displays the result.
    """
    print("\n" + "=" * 40)
    print("  Welcome to the Life Path Number Calculator!")
    print("=" * 40 + "\n")

    # Prompt user for their birth date
    day = int(input("Enter your birth day (1-31): "))
    month = int(input("Enter your birth month (1-12): "))
    year = int(input("Enter your birth year (e.g., 2000): "))

    # Calculate life path number
    life_path_number = calculate_life_path_number(day, month, year)

    # Display the result
    print("\n" + "-" * 40)
    print(f"  Your Life Path Number is: {life_path_number}")
    print("-" * 40 + "\n")


if __name__ == "__main__":
    main()
