# Script Name:	                python-File-Handling
# Author:				        Juan Maldonado
# Date of lastest revision:		12/08/2023
# Purpose:				        This program creates a file, opens it, and manipulates it. 

import os

# This asks for the directory
directory = input("Enter the desired directory (relative or absolute path): ")

# This creates a directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Created directory: {directory}")

# This asks users input for the file name 
file_name = input("Enter the desired file name (include .txt extension): ")
file_path = os.path.join(directory, file_name)

# This allows the user append to the file
while True:
    # This opens the file in append mode
    with open(file_path, 'a') as file:
        # This gets user input for text to append
        text_to_append = input("Enter text to append (or 'exit' to finish): ")

        # This checks if the user wants to exit
        if text_to_append.lower() == 'exit':
            break

        # This appends the text to the file
        file.write(text_to_append + '\n')

# This reads and prints the contents of the file.

with open(file_path, 'r') as file:
    file_contents = file.read()
    print("\nFile Contents:\n", file_contents)

# This delete the .txt file
# If you want, you can comment this section out to see the created text file.
# I did it, but use control z since spacing in python matters. 
try:
    os.remove(file_path)
    print(f"\n{file_path} deleted successfully.")
except FileNotFoundError:
    print(f"\n{file_path} not found.")
except Exception as e:
    print(f"An error occurred: {e}")

