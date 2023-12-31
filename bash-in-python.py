# Script Name:	                bash in python
# Author:				        Juan Maldonado
# Date of lastest revision:		12/04/2023
# Purpose:				        This program executes bash commands on a python file.

# it imports a library that allows operating system interaction
import os

# methods
# This method will run the bash commands
def bash_commands(command):
    result = os.popen(command).read()
    return result

# This will keep asking users for what they want to choose unless they exit.
while True:
    # Display menu options
    print("\nBash Menu Options")
    print("1. Run whoami command")
    print("2. Run ip a command")
    print("3. Run lshw -short")
    print("4. Exit")

    # This collects users choice
    user_choice = input("Enter your choice (1-4): ")

    # Runs the bash command user chose 
    options = {
        '1': lambda: print("Runnung whoami command now:", bash_commands('whoami').strip()),
        '2': lambda: print("\nRunning ip a command:", bash_commands('ip a').strip()),
        '3': lambda: print("\nRunning lshw -short command:", bash_commands('lshw -short').strip()),
        '4': lambda: exit("Exiting the Menu now.")
    }

    # This gets lambda function to use in running commands
    selected_option = options.get(user_choice, None)

    # this executes lamda function, uless its not a valid choice.
    if selected_option:
        selected_option()
    else:
        print("Invalid choice. Please enter a number 1-4: ")


    # This lets users know that the input is invalid.
    options.get(user_choice, lambda: print("The choice you put was not a valid one.\nPlease enter a whole number between 1-4"))
    
