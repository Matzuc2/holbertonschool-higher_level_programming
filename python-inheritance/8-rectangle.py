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

    This class provides a placeholder method for calculating area and a
    method for validating integer values.
    """

    def area(self):
        """
        Placeholder method for calculating the area.

        This method should be implemented by subclasses.

        Raises:
            NotImplementedError: This exception is raised to indicate
            that the method should be implemented by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the provided value is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if type(name) is not str:
            raise TypeError("name of parameter must be a string")
        elif type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from `BaseGeometry`.

    Attributes:
    -----------
    __width : int
        The width of the rectangle.
    __height : int
        The height of the rectangle.

    Methods:
    --------
    __init__(self, width, height)
        Initializes the rectangle with width and height, validating them.
    __str__(self)
        Returns a string representation of the rectangle.
    area(self)
        Computes and returns the area of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height, validating them.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
