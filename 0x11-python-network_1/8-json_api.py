#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if len(sys.argv) == 2:
    q = sys.argv[1]
else:
    q = ""

data = {'q': q}

response = requests.post('http://0.0.0.0:5000/search_user', data=data)

try:
    json_data = response.json()
    if json_data:
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")

