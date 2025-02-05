#!/usr/bin/python3
"""
Module: base_geometry
This module defines the `BaseGeometry` class and the `Rectangle` class
that inherits from `BaseGeometry`. The `BaseGeometry` class includes
methods for geometric operations, and `Rectangle` extends this to
represent a rectangle with validation for its dimensions.
"""


class BaseGeometry:
    """
    A base class for geometric operations.
    """

    def area(self):
        """
        Placeholder method for calculating the area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the provided value is an integer greater than 0.
        """
        if type(name) is not str:
            raise TypeError("name of parameter must be a string")
        elif type(value) is not int or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
