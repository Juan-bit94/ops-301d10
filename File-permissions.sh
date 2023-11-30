#! /bin/bash

# Script Name:                          File-permission.sh
# Author:                               Juan Maldonado
# Date of latest revision:              11/29/2023
# Purpose:                              This script alters file permissions of everything in a directory


# variables 
current_date=$(date '+%Y-%m-%d')
# Welcome message 
echo "Hello, welcome to the file permissions script."

# Asks user for directory path for permission modification
echo "Please enter a directory path so we can modify the file permission: " 
read Dir_path

# Asks user for permission number
echo "Enter the permissions number (example: 777) or notation (a+rw): " 
read permissions 

# This asks for a log file name to record actions taken by script.
echo "Enter the log file name (ex: change_permissions_log_$current_date.txt):" 
read log_file
log_file=${log_file:-change_permissions_log.txt}

# This navigates to the input directory 
cd "$Dir_path" || exit

# This creates the log file
echo -e "Log File - Permissions script used on $(date)\n" > "$log_file"

# method

# this method changes permissions 
change_permissions() {
    for file in *; do 
        if [ -f "$file" ]; then 
        echo "Changing permissions of $file to $permissions"
        chmod "$permissions" "$file"
        echo "$(date) - Changed permissions of $file to $permissions" >> "$log_file"
        sleep 0.1 
    fi 
done 
}
 
# calls method to change permissions of all files in the directory. 
change_permissions

# This prints directory contents and new permissions settings
echo -e "\nDirectory contents:"
ls -l

echo -e "\nNew permissions settings:"
ls -l | awk '{print $1, $9}'

echo -e "\nLog file created: $log_file"