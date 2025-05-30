#!/usr/bin/python3
"""
Module: geometry
This module defines the `BaseGeometry` class, the `Rectangle` class
that inherits from `BaseGeometry`, and a `Square` class that
inherits from `Rectangle`.
"""


class BaseGeometry:
    """
    A base class for geometric operations.

    This class provides a method to validate integer values, ensuring
    they are positive integers greater than 0.
    """

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
    A class used to represent a Rectangle, inheriting from `BaseGeometry`.

    Attributes:
    -----------
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.

    Methods:
    --------
    __init__(self, width, height)
        Initializes the `Rectangle` with width and height, validating them
        as positive integers.
    __str__(self)
        Returns a string representation of the Rectangle in the format
        [Rectangle] width/height.
    area(self)
        Returns the area of the Rectangle (width * height).
    """

    def __init__(self, width, height):
        """
        Initializes the `Rectangle` with width and height, validating
        them as positive integers.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: A string in the format [Rectangle] width/height.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area of the Rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from `Rectangle`.

    The `Square` class uses the `Rectangle` class's validation method
    and defines its own area method for calculating the area of a square.
    """

    def __init__(self, size):
        """
        Initializes the `Square` with a given size, validating it as an
        integer.

        Args:
            size (int): The size of the square (side length).
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the Square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
