def main():
    n = int(input("Enter the number of elements: "))

    numbers = []
    for _ in range(n):
        num = float(input("Enter a number: "))
        numbers.append(num)

    num_positive = sum(1 for num in numbers if num > 0)
    num_negative = sum(1 for num in numbers if num < 0)
    num_zeros = sum(1 for num in numbers if num == 0)
    num_odd = sum(1 for num in numbers if num % 2 != 0)
    num_even = sum(1 for num in numbers if num % 2 == 0)
    average = sum(numbers) / n if n != 0 else 0

    print(f"Number of positive numbers: {num_positive}")
    print(f"Number of negative numbers: {num_negative}")
    print(f"Number of zeros: {num_zeros}")
    print(f"Number of odd numbers: {num_odd}")
    print(f"Number of even numbers: {num_even}")
    print(f"Average of all numbers: {average}")


if __name__ == "__main__":
    main()
