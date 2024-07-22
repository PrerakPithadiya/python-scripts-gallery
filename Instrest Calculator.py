def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    :param principal: The principal amount
    :param rate: The rate of interest per year
    :param time: The time the money is invested or borrowed for, in years
    :return: Simple interest
    """
    return (principal * rate * time) / 100


def calculate_compound_interest(principal, rate, time, n):
    """
    Calculate compound interest.

    :param principal: The principal amount
    :param rate: The rate of interest per year
    :param time: The time the money is invested or borrowed for, in years
    :param n: The number of times interest is compounded per year
    :return: Compound interest
    """
    amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    return amount - principal


def main():
    # Take user inputs
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (per year): "))
    time = float(input("Enter the time period (in years): "))
    n = int(input("Enter the number of times interest is compounded per year: "))

    # Calculate simple interest
    simple_interest = calculate_simple_interest(principal, rate, time)
    print(f"Simple Interest: {simple_interest}")

    # Calculate compound interest
    compound_interest = calculate_compound_interest(principal, rate, time, n)
    print(f"Compound Interest: {compound_interest}")


if __name__ == "__main__":
    main()
