# python3
print("PROGRAM STARTED")
import random
import string
import re
from datetime import datetime


def generate_password(length, use_digits=True, use_symbols=True):
    """Generate a secure password based on user preferences."""

    if length < 8:
        print("❌ Password length must be at least 8.")
        return None

    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))

    return generated_password


def check_password_strength(password):
    """Evaluate password strength using regex."""

    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return "Strong"

    elif len(password) >= 6:
        return "Medium"

    else:
        return "Weak"


def log_password(password, strength):
    """Save password logs with timestamp."""

    try:
        with open("password_log.txt", "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} | {password} | {strength}\n")
    except Exception as error:
        print(f"⚠️ Logging error: {error}")


def display_menu():
    """Show CLI menu."""
    print("\n" + "=" * 40)
    print("🔐 PASSWORD GENERATOR TOOL")
    print("=" * 40)
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")
    print("=" * 40)


def generate_password_flow():
    """Handle password generation process."""

    try:
        length = int(input("Enter password length (min 8): "))

        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_digits, use_symbols)

        if password:
            strength = check_password_strength(password)

            print("\n✅ Generated Password:", password)
            print("🔎 Strength:", strength)

            if strength == "Strong":
                print("💪 Very Secure Password!")
            elif strength == "Medium":
                print("⚠️ متوسط Security")
            else:
                print("❌ Weak Password")

            log_password(password, strength)

    except ValueError:
        print("❌ Invalid input. Please enter a number.")


def check_password_flow():
    """Handle password strength checking."""

    password = input("Enter password to check: ")
    strength = check_password_strength(password)

    print("🔎 Strength:", strength)

    log_password(password, strength)


def main():
    """Main program loop."""

    while True:
        display_menu()
        user_choice = input("Select an option (1-3): ")

        if user_choice == "1":
            generate_password_flow()

        elif user_choice == "2":
            check_password_flow()

        elif user_choice == "3":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()