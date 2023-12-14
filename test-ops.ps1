# Script Name:	                ops-challenge-psutil.py
# Author:				                Juan Maldonado
# Date of lastest revision:		  12/13/2023
# Purpose:				              This program creates a new user in AD.

# Define user information
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$username = "ferdi"
$email = "ferdi@GlobeXpower.com"
$office = "Springfield"
$department = "TPS"
$jobTitle = "TPS Reporting Lead"
$company = "GlobeX USA"

# Specify the organizational unit (OU) where the user will be created
$ou = "OU=Test-Generated-Users,DC=CORP,DC=GLOBEXPOWER,DC=COM"

# Generate a password for the new user
$password = ConvertTo-SecureString -AsPlainText "P@ssw0rd" -Force

# Create a new user in Active Directory
New-ADUser -SamAccountName $username -UserPrincipalName "$username@$env:USERDNSDOMAIN" -Name $displayName -GivenName $firstName -Surname $lastName -EmailAddress $email -Office $office -Department $department -Title $jobTitle -Company $company -Enabled $true -PasswordNeverExpires $true -ChangePasswordAtLogon $false -AccountPassword $password -Path $ou
