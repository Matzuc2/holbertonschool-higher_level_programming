#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Module: 3-is_kind_of_class

    This module defines a function that checks if an object is an instance
    of, or if the object is an instance of a class
    that inherited from, the specified class.
    """

    """
        Check if an object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class.

        Args:
            obj: The object to check.
            a_class: The class to compare against.

        Returns:
            bool: True if the object is an instance
             or inherited instance of the class, False otherwise.
        """
    if isinstance(obj, a_class):
        return True
    else:
        return False
