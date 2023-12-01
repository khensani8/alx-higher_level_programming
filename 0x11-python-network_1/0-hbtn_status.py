#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print(f"- type: {type(content)}")
        print(f"- content: {content.decode('utf-8')}")
        print("- utf8 content: OK$")
except urllib.error.URLError as e:
    print(f"Error fetching URL: {e}")
