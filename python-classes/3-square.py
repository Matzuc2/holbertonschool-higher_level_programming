#!/usr/bin/python3
"""
This module defines the `Square` class.
The class provides functionality to create a square
object with a specified size
and calculate its area.
"""


class Square:
    """
    Represents a square with a specific size.

    Attributes:
        __size (int): The size of the square's
        side, must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square's side (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):  # Validate that size is an integer
            raise TypeError("size must be an integer")
        if size < 0:  # Validate that size is non-negative
            raise ValueError("size must be >= 0")
        self.__size = size  # Set the private size attribute

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square(size * size).
        """
        return self.__size * self.__size
