# Script Name:	                Python-Requests-Library.py
# Author:				        Juan Maldonado
# Date of lastest revision:		12/12/2023
# Purpose:				        This program will perform HTTP GET requests using the requests Python library.

import requests

# This greats user and lets them know what the script will do.
print("Welcome to the Python-Requests-Library script.")
print("This program allows you to send HTTP requests, translate response codes, and perform GitHub authentication.")

# This prompts the user to input the destination URL
website = input("Enter the destination URL: ")
url = str("https://" + website)

# This asks the user to select an HTTP method
http_method = input("Select an HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# This prints the entire request to the screen and asks user for confirmation
print(f"\nRequest to be sent:\nURL: {url}\nHTTP Method: {http_method}")
confirmation = input("\nDo you want to proceed? (yes/no): ")

# This checks if the user wants to proceed
if confirmation.lower() != 'yes':
    print("Request canceled.")
else:
    try:
        # This performs the request with the selected HTTP method
        response = requests.request(http_method, url, timeout=(3, 7))  # Adding timeouts (3 seconds for connection, 7 seconds for read)

        # This translates response status code into human readable terms
        status_code_translation = {
            200: 'All good',
            201: 'Created',
            204: 'No Content Found',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not Found',
            405: 'Method Not Allowed',
            500: 'Internal Server Error',
        }

        # This prints translated status to the screen
        translated_status = status_code_translation.get(response.status_code, 'Unknown Status Code')
        print(f"\nResponse Status: {translated_status}")

        # This prints response header information to the screen
        print("\nResponse Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        # This perform authentication into api.github.com
        # I generated a token by going to my GitHub account and generating a token
        github_auth = ('your_username', 'your_token')  # Replace with your GitHub username and token
        github_response = requests.get('https://api.github.com/user', auth=github_auth, timeout=(3, 7))

        # This prints GitHub response
        print("\nGitHub User Info:")
        print(github_response.json())
    # This lets user know about time out issues.
    except requests.Timeout:
        print("\nError: Request timed out.")
    except requests.RequestException as e:
        print(f"\nError: {e}")
