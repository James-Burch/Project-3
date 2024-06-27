import gspread
from google.oauth2.service_account import Credentials
import getpass

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
    Save new user details to the google sheet so they can login in future
    """
    try:
        worksheet.append_row([username, password])
        print(f"User {username} successfully registered!") 
    except Exception as e:
        print(f"Error registering user {username}: {e}") 

def log_workout(worksheet, username, workout_type):
    """
    Log a workout for the specific user that has logged in 
    """
    exercises = []
    for i in range(1, 6): # Loops 5 times as there are 5 exercises, change range to add or decrease exercises
        exercise_name = input(f"Enter Exercise {i} Name for {workout_type.capitalize()} (or press Enter to skip): ").strip()
        if not exercise_name:
            break # Loop stops if an invalid exercise is entered
        weight = input(f"Enter weight in kg for exercise {i}: ").strip()
        sets = input(f"Enter number of sets for exercise {i}: ").strip()
        reps = input(f"Enter number of reps for exercise {i}: ").strip()

        exercises.append([exercise_name, weight, sets, reps])

    user_exists, row_number = check_user(worksheet, username)

    if user_exists:
            # Gets the current information in the row if the user exists
        row_data = worksheet.row_values(row_number)
            # Adds the new data to the row starting from row C to avoid over writing username and password
        updated_row_data = row_data[:2] + [""] * 3 + sum(exercises, [])

        try:
            worksheet.update(f'A{row_number}', [updated_row_data])
            print(f"Your workout has been logged successfully {username}!")  
        except Exception as e:
            print(f"Error logging workout for {username}: {e}")  
    else:
        print(f"Username '{username}' not found in the database.")        



def menu(username):
    """
    Show menu for the user to select what they want to do once logged in
    """
    while True:
        print("Menu:")
        print("1. Log a workout")
        print("2. View progress")
        print("3. Logout")
        
        menu_choice = input("Please enter a number to select one of the above: ").strip()

        if menu_choice == '1':
            workout_type = choose_workout_type()
            if workout_type:
                log_workout(WORKSHEET, username, workout_type)
                print("Loading workout options")
        elif menu_choice == '2':
            print('Loading progress')
        elif menu_choice == '3':
            print("User has now been logged out")
            main()
        else:
            print("Invalid entry. Please enter '1','2','3' to select an option")

def choose_workout_type():
    """
    Allows the user to select a workout type from 'push', 'pull' or 'legs'.
    It then returns the chosen workout type or None if an incorrect input is selected. 
    """
    while True:
        print("Choose your workout type:")
        print("1. Push")
        print("2. Pull")
        print("3. Legs")

        workout_choice = input("Select 1, 2 or 3 to start logging your workout: ").strip()

        if workout_choice == '1':
            return 'push'
        elif workout_choice == '2':
            return 'pull'
        elif workout_choice == '3':
            return 'legs'
        else:
            print("Invalid choice please choose 1 'push', 2 'pull', 3 'legs'.")                



def main():
    """
    Main function to run the app.
    """
    while True:
        action = input("Do you want to login or signup? (type login or signup and press enter): ").strip().lower()
        if action not in ['login', 'signup']:
            print("Invalid entry please enter 'login' or 'signup'.")
            continue

        username = input("Please enter your username here (press enter to continue): ").strip()
        user_exists, row = check_user(WORKSHEET, username)
    # If the user selects login run this code
        if action == 'login':
            if user_exists:
                password = input('Please enter your password (press enter to continue): ').strip()
                if check_password(WORKSHEET, row, password):
                    print("Login Successful!")
                    menu(username)
                    break
                else:
                    print("Incorrect password. Please try again.")   
            else:
                print("Username does not exist. Please signup or try again.")
    # Else if the user selects signup run this code            
        elif action == 'signup':
            if user_exists:
                print("Username already exists. Please login")
            else:
                password = input("Please enter your password: ").strip()
                register_new_user(WORKSHEET, username, password)
                menu(username)
                break

if __name__ == "__main__":
    main()