#!/usr/bin/python3
"""
This module defines the `Square` class.
The class provides functionality to create a square object with
size and position,
calculate its area, and print a visual representation of the square.
"""


class Square:
    """
    Represents a square with a specific size and position.

    Attributes:
        __size (int): The size of the square (length of one side).
        __position (tuple): The position of the square, defined
        as a tuple of
        two positive integers (x, y) for horizontal and vertical offset.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.

        Args:
            size (int): The size of the square's
            side (default is 0).
            position (tuple): A tuple of two positive integers representing
            the position (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position
             is not a tuple of 2 positive integers.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The position of the square as a tuple of two integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Args:
            value (tuple): A tuple of two positive
             integers representing the position.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints the square using the `#` character. The square's position
        is respected
        by adding horizontal and vertical spacing before the square appears.

        If the size of the square is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for h in range(self.__position[1]):
                    print()
            for i in range(0, self.__size):
                for n in range(self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print('#', end="")
                print()
