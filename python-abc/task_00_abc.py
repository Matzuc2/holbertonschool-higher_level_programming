#!/usr/bin/python3
"""
This module defines the `Square` class.

The class provides functionality to create a square object with a specified
size and position, calculate its area, and print a visual representation.
"""


class Square:
    """
    Represents a square with a specific size and position.

    Attributes:
        __size (int): The size of the square (length of one side).
        __position (tuple): The position of the square, defined as a tuple
        of two non-negative integers (x, y) for horizontal and vertical offset.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.

        Args:
            size (int): The size of the square's side (default is 0).
            position (tuple): A tuple of two non-negative integers representing
            the position (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
            of two non-negative integers.
            ValueError: If size is negative.
        """
        self.size = size  # Use setter to validate
        self.position = position  # Use setter to validate

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square as a tuple of two non-negative
            integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two non-negative integers.

        Raises:
            TypeError: If value is not a tuple of two non-negative integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
