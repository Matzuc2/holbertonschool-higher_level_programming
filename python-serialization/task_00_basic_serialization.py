#!/usr/bin/python3
"""
This module provides functions for serializing and deserializing
Python objects using the pickle module.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes an object and saves it to a file.

    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes an object from a file.
    """
    with open(filename, "r") as file:
        return json.load(file)
