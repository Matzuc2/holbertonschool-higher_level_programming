#!/usr/bin/python3
"""
Module: base_geometry
This module defines the `BaseGeometry` class, which includes methods for
geometric operations.
"""


class BaseGeometry:
    """
    A base class for geometric operations.

    This class provides methods for calculating area and validating
    integer values.
    """

    def area(self):
        """
        Raises an Exception indicating that the `area` method
        is not implemented.

        Raises:
            Exception: Always raises an exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
