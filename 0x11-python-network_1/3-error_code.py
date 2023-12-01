#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
except urllib.error.URLError as e:
    print("Error:", e.reason)
