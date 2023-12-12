# Script Name:	                ops-challenge-psutil.py
# Author:				        Juan Maldonado
# Date of lastest revision:		12/11/2023
# Purpose:				        This program uses the psutil library to add fuctions that fetch system info.

# This imports the psutil module, it allows us to retrieve system info
import os
# 
import psutil

# This gets system information
def system_main_info():
    # This is a dictionary to store info using psutil
    info = {
        'User Mode Time': psutil.cpu_times().user,
        'Kernel Mode Time': psutil.cpu_times().system,
        'Idle Time': psutil.cpu_times().idle,
        'Priority User Mode Time': psutil.cpu_times().nice,
        'I/O Wait Time': psutil.cpu_times().iowait,
        'Hardware Interrupt Time': psutil.cpu_times().irq,
        'Software Interrupt Time': psutil.cpu_times().softirq,
        'Virtualized OS Time': psutil.cpu_times().steal,
        'Gust OS Time': psutil.cpu_times().guest,
    }
    return info

# This saves info to a text file
def save_to_file(info):
    # This is where the info will be saved
    file_path = 'system_info.txt'
    # This opens the file in write mode ('w') 
    with open(file_path, 'w') as file:
        # This writes items in the info dictionary to the file
        for key, value in info.items():
            file.write(f'{key}: {value}\n')
    return file_path

# This displays the info and the directory location for the file
def display_info(file_path):
    # This opens file in read mode
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print(f'File Contents:\n{file_contents}')
    # This gets the directory path of the file.    
    directory_location = os.path.abspath(file_path)
    print(f'\nDirectory Location:\n{directory_location}')

#This checks if the script is being run as the main program
if __name__ == "__main__":
    # This gets the system information using the get_system_info function
    system_info = system_main_info()
    # This saves the system info t0 a text file and it gets the file path
    saved_file_path = save_to_file(system_info)
    # This displays the contents fo the file and directory path
    display_info(saved_file_path)
