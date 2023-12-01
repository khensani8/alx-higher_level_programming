#!/usr/bin/python3
"""A  script that:
- takes in a URL and an email address
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response.
"""
import requests
import sys


if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}

response = requests.post(url, data=data)
print(response.text)
