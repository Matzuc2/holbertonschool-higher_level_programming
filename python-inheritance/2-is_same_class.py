#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Module: 2-is_same_class

    This module contains a function `is_same_class` that checks
      if an object is exactly an instance of a specified class.

    Function:
        is_same_class(obj, a_class):
            Checks if the object is exactly an instance of the specified class.

            Parameters:
                obj: The object to check.
                a_class: The class to match the type of obj against.

            Returns:
                bool: True if obj is exactly an instance of
                a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
