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
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of the square.
        """
        return (self.__size ** 2)

    @property
    def position(self):
        """
        Getter for the position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.
        """
        if not isinstance(value, tuple) or len(value) != 2 or type(value[0])\
            is not int or value[0] < 0 or type(value[1]) is not int\
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """
        Getter for the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
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
        """
        if self.__size == 0:
            print()
            return
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print('#', end="")
                print()
