#!/usr/bin/python3
""" Module: base_geometry """


class BaseGeometry:
    """Defines methods for geometric shapes."""

    def area(self):
        """Calculate the area of a geometric shape.

        Raises:
            Exception: if the area method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): the name of the value.
            value (int): the value to validate.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        """
        if type(value) is not int and not isinstance(int, value):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class used to represent a Rectangle, inheriting BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height, validating them."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
