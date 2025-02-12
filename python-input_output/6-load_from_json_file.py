#!/usr/bin/python3
"""
This module provides a function to create a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)
