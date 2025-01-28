#!/usr/bin/python3
"""
This module defines the `Square` class.
The class provides functionality to create a square
object with a specified size.
"""


class Square:
    """
    Represents a square with a specific size.

    Attributes:
        __size (int): The size of the square's side (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square's side.

        Note:
            The size is stored as a private attribute `__size`.
        """
        self.__size = size
