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
        pass

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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle.

    This class inherits from `BaseGeometry` and represents a rectangle
    by validating its dimensions (width and height) using the
    `integer_validator` method.
    """

    def __init__(self, width, height):
        """
        Initializes a `Rectangle` instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If `width` or `height` are not integers.
            ValueError: If `width` or `height` are less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
