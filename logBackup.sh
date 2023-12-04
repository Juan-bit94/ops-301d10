#! /bin/bash

# Script Name:				logBackup.sh
# Author:				Juan Maldonado
# Date of lastest revision:		11/30/2023
# Purpose:				backup and clear logs


# Variable

# This is where backups will be stored
backup_location="/var/log/backups"

# This creates a backup directory
# if there are none in the location
mkdir -p "$backup_location"

# method

# This prints file size
print_size() {
	file="$1"
	size=$(du -h "file" | cut -f1)
	echo "The file size of $file is: $size" 
}

# This compresses the file

file_compression() {
	compress_file="$1"
	time_stamp=$(date '+%Y%m%d%H%M%S')
	compressed_file="$backup_location/$(basename "$compress_file")-$time_stamp.zip" 

# This prints original file size
print_file_size "$compress_file"

# This compresses the file using gzip
gzip -c "$compress_file" > "$compressed_file"

# This clears the contents of the log file
truncate -s O $compress_file"

# This prints the compressed file size
print_file_size "$compressed_file" 

}

# This lists the lof files to process 

log_files=("/var/log/syslog" "/var/log/wtmp")

# This compresses files
for file in "${log_files[@]}; do
	if [ -f "file" ]; then
	       compress_log_file "$file"
       else 
echo "Log file: $file does not exist."
	fi
done 

