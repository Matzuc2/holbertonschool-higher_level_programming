#!/usr/bin/python3
"""
Module: base_geometry
This module defines the `BaseGeometry` class, which includes a method
to calculate the area. However, the `area` method is not implemented
and raises an exception.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    This class includes a method `area`, which is intended to be
    implemented by subclasses but currently raises an exception.
    """

    def area(self):
        """
        Raises an Exception indicating that the `area` method
        is not implemented.

        Raises:
            Exception: Always raises an exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")
