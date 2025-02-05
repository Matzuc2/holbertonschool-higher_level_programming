#!/usr/bin/python3
"""
Module: base_geometry
This module defines the `BaseGeometry` class and the `Rectangle` class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from `BaseGeometry`.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height, validating them.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
