# task03.py

# Mock database using nested dictionaries and sets
users = {
    101: {
        "name": "Ali",
        "age": 22,
        "skills": {"python", "cpp"}
    },
    102: {
        "name": "Sara",
        "age": 21,
        "skills": {"java", "python"}
    },
    103: {
        "name": "Ahmed",
        "age": 23,
        "skills": {"cpp", "go"}
    }
}


def view_all_users():
    """Display all users in the database."""
    for user_id, data in users.items():
        print("\n----------------------")
        print(f"ID: {user_id}")
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Skills: {', '.join(data['skills'])}")
    print("\n----------------------")


def search_user():
    """Search user using O(1) dictionary lookup."""
    try:
        user_id = int(input("Enter user ID: "))

        if user_id in users:
            print("\nUser Found:")
            user = users[user_id]
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")
            print(f"Skills: {', '.join(user['skills'])}")
        else:
            print("User not found")

    except ValueError:
        print("Invalid input. Please enter a number.")


def show_common_skills():
    """Show common skills between two users using set intersection."""
    common = users[101]["skills"] & users[102]["skills"]
    print(f"Common Skills (User 101 & 102): {', '.join(common)}")


def main():
    """Main menu system using while loop."""
    while True:
        print("\n===== USER MANAGEMENT SYSTEM =====")
        print("1. View All Users")
        print("2. Search User by ID")
        print("3. Show Common Skills (101 & 102)")
        print("Type 'quit' to exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_users()

        elif choice == "2":
            search_user()

        elif choice == "3":
            show_common_skills()

        elif choice.lower() == "quit":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()