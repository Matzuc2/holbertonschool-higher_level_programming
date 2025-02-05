#!/usr/bin/python3
"""
Module: geometry
This module defines the `BaseGeometry` class, the `Rectangle` class,
and the `Square` class that inherits from `Rectangle`.
"""


class BaseGeometry:
    """
    A base class for geometric operations.
    """

    def integer_validator(self, name, value):
        """
        Validates that the provided value is an integer greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from `BaseGeometry`.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height, validating them.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Computes and returns the area of the rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from `Rectangle`.
    """

    def __init__(self, size):
        """
        Initializes the square with the given size, validating it.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # Call Rectangle's constructor
        self.__size = size  # Store size separately if needed

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
