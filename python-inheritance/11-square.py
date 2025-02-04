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
    __width : int
        The width of the rectangle (private)
    __height : int
        The height of the rectangle (private)

    Methods
    -------
    __init__(self, width, height)
        Initializes the Rectangle with width and height
          validating them as integers.
    __str__(self)
        Returns a string representation of the Rectangle.
    area(self)
        Computes and returns the area of the Rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height,
          validating them as integers.

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
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        Computes and returns the area of the Rectangle.

        Returns
        -------
        int
            The area of the rectangle (width * height)
        """
        return (self.__width * self.__height)


class Square(Rectangle):
    """
    This module defines a Square class that inherits from Rectangle.
    """

    """
    A class used to represent a Square, which is a type of Rectangle.

    Methods
    -------
    __init__(self, size)
        Initializes a new Square instance with the given size.

    area(self)
        Returns the area of the square.

    __str__(self)
        Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Parameters
        ----------
        size : int
            The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns
        -------
        str
            A string in the format [Square] <size>/<size>.
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))
