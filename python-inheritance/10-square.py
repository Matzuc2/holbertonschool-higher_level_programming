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
        The width of the rectangle.
    __height : int
        The height of the rectangle.

    Methods
    -------
    __init__(self, width, height)
        Initializes the rectangle with width and height.
    __str__(self)
        Returns a string representation of the rectangle.
    area(self)
        Computes and returns the area of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height.

        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns
        -------
        str
            A string in the format "[Rectangle] width/height".
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns
        -------
        int
            The area of the rectangle.
        """
        return (self.__width * self.__height)


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Methods:
        __init__(self, size): Initializes a Square instance with a given size.
        area(self): Returns the area of the square.
        __str__(self): Returns a string representation of the
        square in the format [Rectangle] size/size.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return str("[Rectangle] {}/{}".format(self.__size, self.__size))
