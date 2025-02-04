#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly)
      from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class
          that inherited
        from the specified class; otherwise False.
    """
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
