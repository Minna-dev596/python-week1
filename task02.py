# Mock database
active_users = []


# ---------------- Helper Functions ---------------- #

def is_valid_name(name):
    return isinstance(name, str) and name.strip() != ""


def is_duplicate(user_list, name):
    return name in user_list


def is_user_eligible(name):
    return is_valid_name(name)


# ---------------- Core Functions ---------------- #

def add_user(user_list, name):
    if not is_user_eligible(name):
        print("Invalid user name.")
        return

    if is_duplicate(user_list, name):
        print("User already exists.")
        return

    user_list.append(name)
    print(f"{name} added successfully.")


def remove_user(user_list, name):
    if name in user_list:
        user_list.remove(name)
        print(f"{name} removed successfully.")
    else:
        print("User not found.")


def check_user(user_list, name):
    if name in user_list:
        print(f"{name} is active.")
    else:
        print(f"{name} is not found.")


# ---------------- Main Program ---------------- #

def main():
    while True:
        print("\n1. Add User")
        print("2. Remove User")
        print("3. Check User")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter user name: ")
            add_user(active_users, name)

        elif choice == "2":
            name = input("Enter user name: ")
            remove_user(active_users, name)

        elif choice == "3":
            name = input("Enter user name: ")
            check_user(active_users, name)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()