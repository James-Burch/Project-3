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
Prior to starting this project I had to decide what to do, I quickly decided that I wanted to do my project on something that is a big part of my life and that I have a passion for, I have recently undergone a big change in the fitness in my own life and thought that I could use this to create a program for logging workouts and tracking progress. I started out creating a lucid chart to allow me to visually see what I needed to implement into my code. This was a massive help as it allowed me to work through step by step and follow a plan to ensure that there were no areas missed out
## User Experience (UX)
### Application Goals
- Add input validation to ensure that any data input by the user is validated, if there is invalid data then the user will be prompted to input new data
- Login/Signup, the user will be prompted to signup if they do not have a username or password, if a user tries to login when they have not signed up they will be asked to signup as the user does not exist
- Once a new user has signed up the application will confirm that the user has been successfully registered
- When the user enters the incorrect password it will tell the user that incorrect password was entered and redirect to login or signup.
- Once the user has signed in they are presented with a clear main menu to choose from 3 different options, where they can log a new workout, view a previous workout or logout.
- Present the user with the option to log 3 different workout types.
### User Stories
- As a user of this programme I want to be able to log my workouts and store the amount of weight, sets and reps I do for each exercise.
- As a user I want to be able to view the previous workout that I have logged to check my previous weight, sets and reps to challenge myself to do more during the next workout.
- As a user I want to be able to receive clear instructions if I input invalid data so that I clearly understand what data is required to be input.
- As a user I want to recieve confirmation of each input, for example when I signup I want to have confirmation that it has been succesfull, or when I login I want to visually see that the login is successful.
- As a user I want the workouts that I have logged to be clearly displayed when I want to view them.
### Data Model
- I have decided to connect a google sheet to my programme, this google sheet hold the username, password and workout information that the specific user logs into the programme.
- The programme will check to see if the user has already got workout data stored, if it has not then the user will not be able to view previous workouts. If the user has got data stored and wants to log a new workout then the new workout will overight the current data.
- 

