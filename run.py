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
    worksheet.append_row([username, password])
    print(f"User {username} successfully registered!") 

def menu():
    """
    Show menu for the user to select what they want to do once logged in
    """
    print("Menu:\n")
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
        user_exists, row = check_user(WORKSHEET, username)


main()