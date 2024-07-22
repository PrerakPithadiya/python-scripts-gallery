import math


def compute_real_roots(a, b, c):
    # Calculate the discriminant
    delta = b**2 - 4 * a * c

    # Check if the discriminant is negative
    if delta < 0:
        return "The equation has no real roots."
    elif delta == 0:
        # Calculate the single root
        root = -b / (2 * a)
        return root
    else:
        # Calculate the two roots
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        return root1, root2


# Take user input for the coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Compute the roots
roots = compute_real_roots(a, b, c)

# Print the results
print("The real roots are:", roots)
