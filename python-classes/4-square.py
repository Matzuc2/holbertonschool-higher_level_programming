#!/usr/bin/python3
"""
This module defines the `Square` class.
The class provides functionality to create a square
object with
a specified size,
calculate its area, and validate the size with property setters and getters.
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
        if not isinstance(size, int):  # Check if size is an integer
            raise TypeError("size must be an integer")
        if size < 0:  # Check if size is non-negative
            raise ValueError("size must be >= 0")
        self.__size = size  # Set the private size attribute

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):  # Validate that size is an integer
            raise TypeError("size must be an integer")
        if value < 0:  # Validate that size is non-negative
            raise ValueError("size must be >= 0")
        self.__size = value  # Update the private size attribute
