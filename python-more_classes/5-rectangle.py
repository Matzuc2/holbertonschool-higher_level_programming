#!/usr/bin/python3
"""
This module defines the `Rectangle` class.
The class provides functionality to create a rectangle object with
width and height, calculate its area and perimeter, and print a visual
 representation of the rectangle.
"""


class Rectangle:
    """
    Represents a rectangle with a specific width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the `#` symbol.

        Returns:
            str: A string representation of the rectangle.
            Returns an empty string if width or height is 0.
        """
        str1 = ""
        for i in range(self.__height):
            for j in range(0, self.__width):
                str1 += "#"
            if i < self.__height - 1:
                str1 += "\n"
        return str1

    def __repr__(self):
        """
        Returns a string representation of the rectangle that
        can be used to recreate a new instance using eval().

        Returns:
            str: A string in the format "Rectangle(width, height)".
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of the rectangle and prints a farewell message.
        """
        print("Bye rectangle...")
