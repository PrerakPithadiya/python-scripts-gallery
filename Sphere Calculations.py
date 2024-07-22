import math


def calculate_sphere_area(radius):
    return 4 * math.pi * radius**2


def calculate_sphere_volume(radius):
    return (4 / 3) * math.pi * radius**3


def main():
    radius = float(input("Enter the radius of the sphere: "))

    area = calculate_sphere_area(radius)
    volume = calculate_sphere_volume(radius)

    print(f"The surface area of the sphere is: {area:.2f}")
    print(f"The volume of the sphere is: {volume:.2f}")


if __name__ == "__main__":
    main()
