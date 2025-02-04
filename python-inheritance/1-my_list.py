#!/usr/bin/python3
"""
Module: 1-my_list
This module defines a class MyList that inherits from the built-in list class.

MyList is a subclass of the built-in list class with
an additional method to print the list in sorted order.

Methods:
    print_sorted: Prints the list in ascending sorted order.
"""


class MyList(list):
    """
    This module defines a class MyList that inherits from the built-in list class.
    A subclass of list that provides a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        """
        print(sorted(self))
