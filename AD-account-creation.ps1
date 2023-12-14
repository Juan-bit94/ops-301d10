# Script Name:   AD-account-creation.ps1
# Author:        Juan Maldonado
# Date of latest revision: 12/13/2023
# Purpose:       This program creates a new user on a OU

# This defines user information
$firstName ="Franz"
$lastName = "Ferdinand"
$displayName ="$firstName $lastName"
$username = "ferdi"
$email = "ferdi@GlobXpower.com"
$office = "Springfield"
$department = "TPS"
$jobTitle = "TPS Reporting Lead"
$company = "GlobeX USA"

# This specifies the organizational unit (OU) where the user will be created
$userOU = "OU=Test-Generated-Users,DC=CORP,DC=GLOBEXPOWER,DC=COM"

# This generates a password for new user
$password = ConvertTo-SecureString -AsPlainText "P@ss0rd" -Force

# debugging line
Write-Host "Username: $username"
Write-Host "UserPrincipalName: $username@$env:USERDNSDOMAIN"
Write-Host "OU Path: $userOU"

# This creates a new user in AD
try {
New-ADUser -SamAccountName $username -UserPrincipalName "$username@$env:USERDNSDOMAIN" -Name $displayName -GivenName $firstName -Surname $lastName -EmailAddress $email -Office $office -Department $department -Title $jobTitle -Company $company -Enabled $true -PasswordNeverExpires $true -ChangePasswordAtLogon $false -AccountPassword $password -Path $userOU
Write-Host "User created successfully."
}
catch {
    Write-Host "Error creating user: $_"
} 