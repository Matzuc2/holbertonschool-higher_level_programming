#!/usr/bin/python3
"""
This module defines an abstract Shape class and its subclasses
Circle and Rectangle.

The Shape class provides a blueprint for geometric shapes with abstract methods
for calculating area and perimeter. The Circle and Rectangle classes implement
these methods.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    Methods:
        area(): Abstract method to calculate the shape's area.
        perimeter(): Abstract method to calculate the shape's perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.

        This method must be implemented by subclasses.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.

        This method must be implemented by subclasses.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.

    Attributes:
        __radius (float): The radius of the circle.

    Methods:
        area(): Returns the area of the circle.
        perimeter(): Returns the perimeter (circumference) of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.__radius = abs(radius)

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.

    Attributes:
        __width (float): The width of the rectangle.
        __height (float): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.

    Args:
        shape (Shape): An instance of a class that inherits from Shape.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
