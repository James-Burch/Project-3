![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Fitness Tracker
## Site Introduction
[Insert Image of console in launched site]
The Fitness Tracker Project is a Python-based application that allows users to log and track their workouts. Users can create an account, log their workouts (categorized as push, pull, or legs), and view their progress over time. The project utilizes Google Sheets for storing user data and workout logs, ensuring that the information is easily accessible and manageable. My inspiration for creating this program came from my own fitness journey, I personally use a fitness tracker to keep me motivated and able to see my progress.
## Project Planning
Prior to starting this project I had to decide what to do, I quickly decided that I wanted to do my project on something that is a big part of my life and that I have a passion for, I have recently undergone a big change in the fitness in my own life and thought that I could use this to create a program for logging workouts and tracking progress. I started out creating a lucid chart to allow me to visually see what I needed to implement into my code. This was a massive help as it allowed me to work through step by step and follow a plan to ensure that there were no areas missed out.
## User Experience (UX)
### Program Goals
- Allow user to signup if they have not already, requires username and password.
- Allow user to login if they have already signed up user their username and password.
- Allow the user to log a workout and store it in the google sheet that is connected using API's
- Allow the user to view previous workout data that they have entered
- Allow the user to clearly and easily navigate the program at each stage so that there is always a valid entry into the console
- Have a response to every single input option at each stage of the program so that the user is never stuck or unsure on what the program needs them to input to carry on using the program
- Allow the user to logout/exit the program once they are finished using it
### User Needs
- As a user of this programme I want to be able to log my workouts and store the amount of weight, sets and reps I do for each exercise.
- As a user I want to be able to view the previous workout that I have logged to check my previous weight, sets and reps to challenge myself to do more during the next workout.
- As a user I want to be able to receive clear instructions if I input invalid data so that I clearly understand what data is required to be input.
- As a user I want to recieve confirmation of each input, for example when I signup I want to have confirmation that it has been succesfull, or when I login I want to visually see that the login is successful.
- As a user I want the workouts that I have logged to be clearly displayed when I want to view them.
### Program Flow
- When the user first enters into the program they are presented with a screen that explains a little bit about what the program can be used for and prompts the user to either select to signup or login

- If the user has selected to signup they will be used to enter a username for their account, after a username has been entered then the user will be asked to enter a password which will only work if the password matches the username it is assigned too. Once the user has entered this data it will be stored in the worksheet that is linked to the program using googlesheets API's

- If the user has selected to login as they have already created an account they will need to enter their username, the program will then check that it has that username (case sensitive) stored in the worksheet attached to the program, if the username matches one stored then the user will need to input the valid password attached to that username, if the user does not input a username that matches one stored in the worksheet then the program will tell the user that the username entered does not exist and will redirect them to signup or login again.

- Once the user is logged in the console will tell the user that they have successfully logged in, it will then load a main menu which displays 3 options. The options are to log a workout, view a previous workout or logout. The user must input 1,2 or 3 to select which one they would like to continue with.
