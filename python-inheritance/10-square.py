#!/usr/bin/python3
""" Module: geometry This module defines the `BaseGeometry` class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from `Rectangle`.
    """

    def __init__(self, size):
        """
        Initializes the square with the given size, validating it.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
