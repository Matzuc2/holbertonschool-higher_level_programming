#!/usr/bin/python3
"""
This module provides a function to write a Python object to a file
using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be serialized and written to the file.
        filename (str): The name of the file where the
        JSON data will be stored.

    Returns:
        None
    """
    with open(filename, "a") as file:
        json.dump(my_obj, file)
