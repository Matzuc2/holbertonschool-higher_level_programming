#!/usr/bin/python3
"""
This module provides a function for reading and displaying
the contents of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
         Defaults to an empty string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an error occurs while reading the file.
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
    print(content, end="")
