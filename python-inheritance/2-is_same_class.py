#!/usr/bin/python3
"""
Module: is_same_class
This module provides a function to check if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Determines if an object is an exact instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class`, otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
