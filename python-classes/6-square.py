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
        return (self.__size * self.__size)

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
        if not isinstance(value, tuple) and len(value) != 2:
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
            for h in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for n in range(self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print('#', end="")
                print()
