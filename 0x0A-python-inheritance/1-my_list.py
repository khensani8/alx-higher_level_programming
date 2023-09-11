#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList:
    """impletments sorted printing from the built-in class"""
    def print_sorted(self):
        """Prints a list in a sorted ascending order"""
        print(sorted(self))
