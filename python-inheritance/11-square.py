#!/usr/bin/python3
"""
Module: geometry
This module defines the `BaseGeometry`, `Rectangle`, and `Square` classes
for geometric operations. The `Rectangle` class inherits from `BaseGeometry`,
and the `Square` class inherits from `Rectangle`.
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
    __width : int
        The width of the rectangle (private).
    __height : int
        The height of the rectangle (private).

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
        Initializes the Rectangle with width and height, validating them.

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
            str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Computes and returns the area of the Rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from `Rectangle`.

    Methods:
    -------
    __init__(self, size)
        Initializes a new Square instance with the given size.
    area(self)
        Returns the area of the square.
    __str__(self)
        Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format "[Square] size/size".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
