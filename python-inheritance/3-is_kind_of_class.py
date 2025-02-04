#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
This module defines a function that checks if an object is an instance
of a specified class or an instance of a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Determines if an object is an instance of a given class or its subclass.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class` or its subclass,
        otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
