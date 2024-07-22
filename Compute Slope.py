def compute_slope(x1, y1, x2, y2):
    # Check if the line is vertical to avoid division by zero
    if x1 == x2:
        raise ValueError("The line is vertical, slope is undefined.")

    # Calculate the slope
    slope = (y2 - y1) / (x2 - x1)
    return slope


# Get input from the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

try:
    slope = compute_slope(x1, y1, x2, y2)
    print(
        f"The slope of the line between points ({x1}, {y1}) and ({x2}, {y2}) is {slope}"
    )
except ValueError as e:
    print(e)
