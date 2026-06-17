# Constants (NO magic numbers)
BONUS_MULTIPLIER = 2


def main():
    # User Input
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_number = float(input("Enter a number: "))

    # Calculation
    calculated_value = user_number * BONUS_MULTIPLIER

    # Output using f-strings
    print(f"\nHello {user_name}!")
    print(f"You are {user_age} years old.")
    print(f"Your number after calculation is: {calculated_value}")


if __name__ == "__main__":
    main()