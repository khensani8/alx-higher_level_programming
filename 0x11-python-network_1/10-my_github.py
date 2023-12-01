#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import requests
import sys
import os


if len(sys.argv) != 3:
    print("Usage: {} <username> <token>".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'

# Set up the request headers with Basic Authentication
headers = {
    'Authorization': 'Basic ' + (username + ':' + token).encode('utf-8').decode('base64')
}

response = requests.get(url, headers=headers)

# Chieck if the request was successful (HTTP status code 200)
if response.status_code == 200:
    json_data = response.json()
    print(json_data['id'])
else:
    print("Error:", response.status_code)
