#!/usr/bin/python3
"""
Module: inherits_from
This module defines a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of a subclass of `a_class`,
        but not an instance of `a_class` itself; otherwise False.
    """
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
