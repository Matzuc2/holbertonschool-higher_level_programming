#!/usr/bin/python3
"""
This module provides a function to convert
a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return (json.dumps(my_obj))
