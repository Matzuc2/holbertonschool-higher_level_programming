#!/usr/bin/python3
"""
This module provides functions for serializing and deserializing
Python objects using the pickle module.
"""

import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serializes an object and saves it to a file.

    """
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes an object from a file.
    """
    with open(filename, "rb") as file:
        return pickle.load(file)
