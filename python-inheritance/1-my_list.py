#!/usr/bin/python3
"""
Module: 1-my_list
This module defines the `MyList` class, which inherits from the built-in
`list` class. It extends `list` by adding a method to print the elements
in sorted order.

Classes:
    MyList: A subclass of `list` that provides an additional method
    for displaying a sorted version of the list.

Methods:
    print_sorted(self): Prints the list elements in ascending order.
"""


class MyList(list):
    """
    A subclass of `list` that includes a method to print the list
    in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
