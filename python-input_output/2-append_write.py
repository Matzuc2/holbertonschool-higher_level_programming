#!/usr/bin/python3
"""
This module provides a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends the given text to a file and
      returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
          Defaults to an empty string.
        text (str): The text to be appended to the file.
          Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a") as file:
        file.write(text)
    return (len(text))
