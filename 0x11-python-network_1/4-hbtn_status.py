#!/usr/bin/python3
"""
requests model
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.content.decode('utf-8')))
print("\t- utf8 content: {}".format(response.text))

