#!/usr/bin/python3
"""
This module provides a function to write text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (str): The name of the file to write
         to (default is an empty string).
        text (str): The text to write into the file
        (default is an empty string).

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w") as file:
        file.write(text)
    return (len(text))
