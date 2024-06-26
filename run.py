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
SHEET = GSPREAD_CLIENT.open('fitness-tracker-project')

# Commented out code as I want a better way to code this

# def check_user(username, password):
#     """
#     Checks the users inputted data to see if it is in the google sheet, 
#     if it is then the user will be signed in, 
#     if it is not then they will be promnpted to signup or try again
#     """
#     users = SHEET.get_all_records()
#     for user in users:
#         if user['Username'] == username and user['Password'] == password:
#             return True
#     return False    

# def signup(username, password):
#     """
#     If the username entered does not match one in the google sheet then the users username will be added and used to signup.
#     They will be asked to enter a password, this will be added alongside their username
#     """    
#     users = SHEET.get_all_records()
#     for user in users:
#         if user['Username'] == username:
#             return False
#     sheet.append_row([username, password])  
#     return True

# def login():
#     """
#     User will enter username and password here to login
#     """
#     while True:
#         print("Please enter a username and password")

#     username = input("Enter your username:\n")
#     password = input("Enter your password:\n")
#     print(username)


def check_user(SHEET, username):
    """
    Check if the username entered is in the list of usernames on sheets.
    """
    usernames = SHEET.col_values(1)
    if username in usernames:
        return True, usernames.index(username) + 1
    return False, None

def check_password(SHEET, column, password):
    """
    Check if password is correct
    """
    stored_password = SHEET.cell(column, 2).value
    return stored_password == password

def register_new_user(SHEET, username, password):
    """ 
    Save new user details to the google sheet so they can login in future
    """
    SHEET.append_row([username, password])
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
        user_exists, row = check_user(SHEET, username)



main()