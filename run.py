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
    print(f"Usernames in the userdata: {usernames}") # Delete once done
    usernames = worksheet.col_values(1)
    if username in usernames:
        return True, usernames.index(username) + 1
    return False, None

def check_password(worksheet, row, password):
    """
    Check if password is correct
    """
    print(f"Stored password: {stored_password}") # Delete once done
    stored_password = worksheet.cell(row, 2).value
    return stored_password == password

def register_new_user(worksheet, username, password):
    """ 
    Save new user details to the google sheet so they can login in future
    """
    print(f"Debug: New user {username} registered with password {password}") # Delete once done
    print(f"Attempting to register user {username} with password {password}")
    worksheet.append_row([username, password])
    print(f"User {username} successfully registered, enjoy!") 

def menu():
    """
    Show menu for the user to select what they want to do once logged in
    """
    print("Menu:")
    print("1. Log a workout")
    print("2. View progress")
    print("3. Logout")


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
        print(f"Entered username: {username}") # Delete once done
        user_exists, row = check_user(WORKSHEET, username)
    # If the user selects login run this code
        if action == 'login':
            if user_exists:
                password = input('Please enter your password (press enter to continue): ').strip()
                print(f"Debug: Entered password: {password}") # Delete once done
                if check_password(WORKSHEET, row, password):
                    print("Login Successful!")
                    menu()
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
            print(f"Debug: Entered password for signup: {password}") # Delete once done
            register_new_user(WORKSHEET, username, password)




main()