import gspread
from google.oauth2.service_account import Credentials
import getpass
from tabulate import tabulate
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET = GSPREAD_CLIENT.open('fitness-tracker-project')
WORKSHEET = SPREADSHEET.worksheet('userdata')


def check_user(worksheet, username):
    """
    Check if the username entered is in the list of usernames on sheets.
    """
    usernames = worksheet.col_values(1)
    if username in usernames:
        print(f"User {username} is correct please enter your password next!\n")
        return True, usernames.index(username) + 1
    return False, None


def check_password(worksheet, row, password):
    """
    Check if password is correct
    """
    stored_password = worksheet.cell(row, 2).value
    return stored_password == password


def register_new_user(worksheet, username, password):
    """
    Register a new user by storing their username and password in google sheets
    """
    try:
        worksheet.append_row([username, password])
        print(f"User {username} successfully registered!\n")
    except Exception as e:
        print(f"Error registering user {username}: {e}\n")


def validate_username(username):
    """
    Check that the username entered is a valid format,
    contains only letters and more than 3 characters
    """
    if re.match("^[A-Za-z]{4,}$", username):
        return True
    else:
        print("Invalid username, Username must contain only letters and 3 or more characters.\n")
        return False


def validate_number(value):
    """
    Validate if a number has been input
    """
    return value.isdigit()

def validate_exercise_name(name):
    """
    Validate that exercise name entered is all letters and has more than 3 characters
    """
    if re.match("^[A-Za-z]{4,}$", name):
        return True
    else:
        print("Invalid exercise name, exercise must contain only letters and be 3 or more characters.\n")    


def log_workout(worksheet, username, workout_type):
    """
    Log a workout for the specific user that is logged in currently.
    """
    print(f"{username} has begun to log a {workout_type} workout.\n")
    exercises = []
    for i in range(1, 6):  # Loops 5 times as there are 5 exercises, change range to add or decrease exercises
        while True:
            exercise_name = input(f"Enter Exercise Name {i} for {workout_type.capitalize()} workout: \n").strip()
            if not exercise_name:
                break  # Loop stops if there is no excercise name entered
            if validate_exercise_name(exercise_name):
                break
        if not exercise_name:
            break

        while True:
            weight = input(f"Enter weight in kg for exercise {i}: ").strip()
            if validate_number(weight):
                break
            else:
                print("Invalid weight. Please enter a number.")

        while True:
            sets = input(f"Enter number of sets for exercise {i}: ").strip()
            if validate_number(sets):
                break
            else:
                print("Invalid number of sets. Please enter a number.")

        while True:
            reps = input(f"Enter number of reps for exercise {i}: ").strip()
            if validate_number(reps):
                break
            else:
                print("Invalid number of reps. Please enter a number.")        
            
            exercises.append([exercise_name, weight, sets, reps])
            
            user_exists, row_number = check_user(worksheet, username)
            
            if user_exists:
        # Gets the current row data if the user exists
                row_data = worksheet.row_values(row_number)
        # Update the row data with new exercises, avoiding overwriting username and password
                updated_row_data = row_data[:2] + sum(exercises, [])

            try:
                worksheet.update(range_name=f'A{row_number}', values=[updated_row_data])
                print(f"Your workout has been logged successfully {username}!\n")
            except Exception as e:
                print(f"Error logging workout for {username}: {e}\n")
        else:
            print(f"Username '{username}' not found in the database.\n")


def menu(username):
    """
    Display the menu for the logged-in user.
    """
    while True:
        print("Menu:")
        print("1. Log a workout")
        print("2. View previous workout")
        print("3. Logout")

        menu_choice = input("Please enter 1, 2 or 3 to select one of the above: \n").strip()

        if menu_choice == '1':
            workout_type = choose_workout_type()
            if workout_type:
                log_workout(WORKSHEET, username, workout_type)
                print("Loading workout options\n")
        elif menu_choice == '2':
            view_progress(WORKSHEET, username)
        elif menu_choice == '3':
            print("User has now been logged out\n")
            break
        else:
            print("Invalid entry. Please enter '1','2','3' to select an option\n")


def choose_workout_type():
    """
    Allows the user to select a workout type from 'push', 'pull' or 'legs'.
    It then returns the chosen workout type or None if an incorrect input is selected.
    """
    while True:
        print("Choose your workout type:/n")
        print("1. Push")
        print("2. Pull")
        print("3. Legs")

        workout_choice = input("Select 1, 2 or 3 to start logging your workout: \n").strip()

        if workout_choice == '1':
            return 'push'
        elif workout_choice == '2':
            return 'pull'
        elif workout_choice == '3':
            return 'legs'
        else:
            print("Invalid choice please choose 1 'push', 2 'pull', 3 'legs'.\n")


def view_progress(worksheet, username):
    """
    Allows the user to pull their previous workout data and compare to their current data in a table
    """
    user_exists, row_number = check_user(worksheet, username)

    if user_exists:
        row_data = worksheet.row_values(row_number)

        if len(row_data) > 2:  # Checks if there is logged data for that user
            headers = ["Exercise", "Weight (kg)", "Sets", "Reps"]
            exercises = [row_data[i:i+4] for i in range(2, len(row_data), 4)]
            print(tabulate(exercises, headers=headers, tablefmt="pretty"))
        else:
            print(f"{username} has no workout data to view.\n")
    else:
        print(f"User {username} not found in database, please log a workout.\n")


def main():
    """
    Main function to run the app.
    """
    print("Welcome to your fitness tracker app, please login or signup to get started!\n")

    while True:
        action = input("Do you want to login or signup? (type login or signup and press enter): \n").strip().lower()
        if action not in ['login', 'signup']:
            print("Invalid entry please enter 'login' or 'signup'.\n")
            continue

        username = input("Please enter your username here (press enter to continue): \n").strip()
        if not validate_username(username):
            continue

        user_exists, row = check_user(WORKSHEET, username)
    # If the user selects login run this code
        if action == 'login':
            if user_exists:
                password = input('Please enter your password (press enter to continue): \n').strip()
                if check_password(WORKSHEET, row, password):
                    print("Login Successful!\n")
                    menu(username)
                    break
                else:
                    print("Incorrect password. Please try again.\n")
            else:
                print("Username does not exist. Please signup or try again.\n")
            # Else if the user selects signup run this code
        elif action == 'signup':
            if user_exists:
                print("Username already exists. Please login")
            else:
                print(f"Username {username} is valid and has been created please enter a password so you are able to log back in future.\n")
                password = input("Please enter your password: /n").strip()
                register_new_user(WORKSHEET, username, password)
                menu(username)
                break


if __name__ == "__main__":
    main()
  