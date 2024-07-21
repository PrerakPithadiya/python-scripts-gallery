def get_valid_input(prompt, type_func):
    """Get valid user input, ensuring it's the correct type and positive."""
    while True:
        try:
            value = type_func(input(prompt))
            if value <= 0:
                raise ValueError("The value must be a positive number.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def get_unit_choice(prompt, choices):
    """Get valid user unit choice from given options."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        else:
            print(f"Invalid choice. Please choose from {', '.join(choices)}.")


def convert_units(weight, height, weight_unit, height_unit):
    """Convert weight and height to metric units if necessary."""
    if weight_unit == "pounds":
        weight *= 0.453592  # Convert pounds to kilograms
    if height_unit == "feet":
        height *= 0.3048  # Convert feet to meters
    elif height_unit == "centimeters":
        height /= 100  # Convert centimeters to meters
    return weight, height


def calculate_bmi(weight, height):
    """Calculate BMI given weight and height."""
    return weight / (height**2)


def determine_bmi_category(bmi):
    """Determine BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    """Main function to run the BMI calculator."""
    print("Welcome to the BMI Calculator 🏋️‍♂️")

    weight_unit = get_unit_choice(
        "Would you like to input your weight in kilograms or pounds? (kilograms/pounds): ",
        ["kilograms", "pounds"],
    )
    height_unit = get_unit_choice(
        "Would you like to input your height in meters, centimeters, or feet? (meters/centimeters/feet): ",
        ["meters", "centimeters", "feet"],
    )

    weight = get_valid_input(f"Enter your weight in {weight_unit}: ", float)
    height = get_valid_input(f"Enter your height in {height_unit}: ", float)

    weight, height = convert_units(weight, height, weight_unit, height_unit)

    bmi = calculate_bmi(weight, height)
    category = determine_bmi_category(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")


if __name__ == "__main__":
    main()
