#!/usr/bin/python3
class BaseGeometry:
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This module defines a Rectangle class that inherits from BaseGeometry.
    """

    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.

    Attributes
    ----------
    width : int
        The width of the rectangle
    height : int
        The height of the rectangle

    Methods
    -------
    __init__(self, width, height)
        Initializes the Rectangle with width and
        height, validating them as integers.
    __str__(self)
        Returns a string representation of the Rectangle.
    area(self)
        Returns the area of the Rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height
        , validating them as integers.

        Parameters
        ----------
        width : int
            The width of the rectangle
        height : int
            The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns
        -------
        str
            A string in the format [Rectangle] width/height
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        Returns the area of the Rectangle.

        Returns
        -------
        int
            The area of the rectangle (width * height)
        """
        return (self.__width * self.__height)


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
