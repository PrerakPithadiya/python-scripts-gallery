import random


# Generate a dictionary with random average daily temperatures (floating-point values)
def generate_random_temperatures():
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    temperatures = {day: round(random.uniform(30.0, 60.0), 1) for day in days_of_week}
    return temperatures


# Function to print days with temperature between 40 and 50 degrees
def print_days_with_temperature_between_40_and_50(temperatures):
    for day, temp in temperatures.items():
        if 40.0 <= temp <= 50.0:
            print(day)


# Generate random temperatures and print the days with temperatures between 40 and 50 degrees
average_temperatures = generate_random_temperatures()
print("Generated Temperatures:", average_temperatures)
print("Days with temperatures between 40 and 50 degrees:")
print_days_with_temperature_between_40_and_50(average_temperatures)
