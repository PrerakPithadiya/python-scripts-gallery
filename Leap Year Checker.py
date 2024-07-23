def is_leap_year(year):
    # A year is a leap year if it is divisible by 4 and (not divisible by 100 or divisible by 400)
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


# Input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
