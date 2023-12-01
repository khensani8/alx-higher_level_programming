#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
request = urllib.request.Request(url, data=data, method='POST')

try:
    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
except urllib.error.URLError as e:
    print("Error:", e.reason)
