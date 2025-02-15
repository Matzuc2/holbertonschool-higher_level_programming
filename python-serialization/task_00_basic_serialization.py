#!/usr/bin/python3
"""
This module provides functions for serializing and deserializing
Python objects using the pickle module.
"""

import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serializes an object and saves it to a file.

    Args:
        data (any): The Python object to serialize.
        filename (str): The name of the file to store the serialized data.

    Returns:
        None
    """
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes an object from a file.

    Args:
        filename (str): The name of the file containing the serialized data.

    Returns:
        any: The deserialized Python object.
    """
    with open(filename, "rb") as file:
        return pickle.load(file)
