#! /bin/bash

# Script Name:                          ops-challenge-append-date-time
# Author:                               Juan Maldonado
# Date of latest revision:              10/24/2023
# Purpose:                              Use time stamping in automated log generation

# Method
stepBystepTime() {
    echo "[ $(date '+%Y-%m-%d %H:%M:%S')] $1"
}

stepBystepTime "Time stamping is a critical step in automating log generation. The syslog will be copied now."

# Declaration of variables
current_date=$(date '+%Y%m%d_%H%M%S')
current_user=$whoami
destination_file="/home/${current_user}/Documents/syslog_${current_date}.log"

cat /var/log/syslog >> $destination_file
# main

stepBystepTime "Syslog was successfully to: $destination_file"
