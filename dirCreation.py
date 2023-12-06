# Script Name:	                dirCreation.py
# Author:				        Juan Maldonado
# Date of lastest revision:		12/05/2023
# Purpose:				        This program generates all directories, sub-directories and files for a user-provided directory path.

# Import libraries
import os

# Delcaration of functions
def directory_list(path_location):
    # Checks user provided path.
    if not os.path.exists(path_location):
        print(f"Sorry, the path you entered '{path_location}' does not exist.")
        return
    
    # Uses os.walk() on directory.
    for (root, dirs, files) in os.walk(path_location):
        # Ouputs current directory
        print(f"Directory: {root}")

        # Output subdirectories
        for dirname in dirs:
            print(f" Subdirectory: {os.path.join(root, dirname)}")

        # Output files
        for filename in files:
            print(f" File: {os.path.join(root, filename)}")

    if __name__ == "__main__":
        # Declaraction of variables
        path_location = input("Enter a directory path (ex: /home/juan/ops-challange): ")

        # Takes user input and puts it into the function.
        directory_list(path_location)

    
