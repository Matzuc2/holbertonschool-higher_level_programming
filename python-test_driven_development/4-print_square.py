#!/usr/bin/python3
def print_square(size):
    """Module that prints a square with the character """

    """Function that prints a square with the character
    Args:
        size: integer
    return:
        None"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
