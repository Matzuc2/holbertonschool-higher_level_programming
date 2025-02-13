#!/usr/bin/python3
"""
This module provides a function to get the dictionary
representation of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
      with simple data structures.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary representation of the object
          with only JSON-serializable attributes.
    """
    return obj.__dict__
