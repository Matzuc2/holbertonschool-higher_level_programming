#!/usr/bin/python3
"""
Module 0-lookup
Contains a single function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the
         attributes and methods of the object.
    """
    return dir(obj)
