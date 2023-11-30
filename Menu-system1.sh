#! /bin/bash

# Script Name:                  Menu-system.sh
# Author:                       Juan Maldonado
# Date of lastest revision:     11/30/2023
# Purpose:                      This script uses conditionals to allow individuals to ping.

# Main

# This will display menu options and accpet user choice
while true;do 

# Menu options
echo -e "\nMenu Options:"
echo "1. Print Hello World"
echo "2. Pring self (loopback address)"
echo "3. IP info (network adpater information for this host)"
echo "4. Exit program"

# User makes a choice 
read -p "Please enter you choice (1-4): " choice

# Executes user choice
if [ "$choice" -eq 1 ]; then  
    echo "Hello World!"
        echo " " 
        echo "You will now be taken back to the menu."
        echo "Please select another option."
elif [ "$choice" -eq 2 ]; then 
    ping -c  6 127.0.01
        echo " " 
        echo "You will now be taken back to the menu."
        echo "Please select another option."
elif [ "$choice" -eq 3 ]; then 
        ifconfig
        echo " " 
        echo "You will now be taken back to the menu."
        echo "Please select another option."
elif [ "$choice" -eq 4 ]; then 
        echo " " 
        echo "You will now exit the program."
        exit 0
else 
        echo " " 
        echo "You have entered an invalid choice. Please enter a number between 1 and 4"
    fi 
done 