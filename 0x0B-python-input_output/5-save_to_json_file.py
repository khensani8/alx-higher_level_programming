#!/usr/bin/python3
"""Defines JSON for saving file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
