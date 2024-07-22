import math


def ladder_length(height, angle_degrees):
    # Convert the angle from degrees to radians
    angle_radians_inner = math.radians(angle_degrees)

    # Calculate the length of the ladder using the sine function
    ladder_length_calc = height / math.sin(angle_radians_inner)

    return ladder_length_calc


# Input: height and angle
height = float(input("Enter the height the ladder needs to reach (in meters): "))
angle_degrees = float(input("Enter the angle of the ladder (in degrees): "))

# Calculate the length of the ladder
length = ladder_length(height, angle_degrees)

# Output the result
print(f"The length of the ladder required is: {length:.2f} meters")
