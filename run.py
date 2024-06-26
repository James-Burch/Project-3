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