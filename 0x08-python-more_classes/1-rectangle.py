#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """ Represents a retangle"""
    def width(self, width=0, heigh=0):
        """Initilises an new Rectangle

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = 0
        self.width = 0

        @property
        def width(self):
            """ Get/set the width of the reactangle"""
            return (self.width)

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.width = value

        @property
        def height(self):
            """Get/set the heigh of the rectangle"""
            return (self.height)

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.height = value
