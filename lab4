def print_menu():
    print("1. Show user list")
    print("2. Add a new user")
    print("3. Edit a user")
    print("4. Delete a user")
    print("5. Log in")
    print("6. Exit")

def add_user(user_list):
    user = {}
    user["Name"] = input("Enter the name: ")
    user["Surname"] = input("Enter the surname: ")
    user["Age"] = input("Enter the age: ")
    user["Address"] = input("Enter the address: ")
    user["Username"] = input("Enter the username: ")

    while True:
        email = input("Enter the email: ")
        if not any(existing_user["Email"] == email for existing_user in user_list):
            user["Email"] = email
            break
        else:
            print("This email is already registered. Try another one.")

    while True:
        password = input("Enter the password (at least 8 characters): ")
        if len(password) >= 8:
            user["Password"] = password
            break
        else:
            print("Password is too short. Please try again.")

    user_list.append(user)
    print("User successfully added!")

def edit_user(user_list):
    username = input("Enter the username of the user to edit: ")

    for user in user_list:
        if user["Username"] == username:
            print("User found. Enter new data:")
            user["Name"] = input("Name: ")
            user["Surname"] = input("Surname: ")
            user["Age"] = input("Age: ")
            user["Address"] = input("Address: ")
            user["Email"] = input("New email: ")
            user["Password"] = input("New password: ")
            print("User successfully edited!")
            return

    print("User with this username not found.")

def delete_user(user_list):
    username = input("Enter the username of the user to delete: ")

    for user in user_list:
        if user["Username"] == username:
            user_list.remove(user)
            print("User successfully deleted!")
            return

    print("User with this username not found.")

def show_users(user_list):
    print("User list:")
    for user in user_list:
        print("Name: {}, Surname: {}, Age: {}, Address: {}, Email: {}, Password: {}".format(
            user["Name"], user["Surname"], user["Age"], user["Address"], user["Email"], user["Password"]
        ))

def login(user_list):
    email = input("Enter the email: ")
    password = input("Enter the password: ")

    for user in user_list:
        if user["Email"] == email and user["Password"] == password:
            print("Login successful!")
            return

    print("Incorrect email or password.")

def main():
    users = []

    while True:
        print_menu()
        choice = input("Choose an action (1-6): ")

        if choice == "1":
            show_users(users)
        elif choice == "2":
            add_user(users)
        elif choice == "3":
            edit_user(users)
        elif choice == "4":
            delete_user(users)
        elif choice == "5":
            login(users)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose from 1 to 6.")

if __name__ == "__main__":
    main()

