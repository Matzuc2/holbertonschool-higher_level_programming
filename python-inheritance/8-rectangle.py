#!/usr/bin/python3
""" Module: base_geometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class used to represent a Rectangle, inheriting BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height, validating them."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
