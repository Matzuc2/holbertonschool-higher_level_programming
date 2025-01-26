#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers, a and b.

    Args:
        a: First number (int or float).
        b: Second number (int or float), default is 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
        ValueError: If a or b is NaN.
        OverflowError: If a or b is infinity.
    """
    if a is None or (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float):
        if a == float('inf') or a == float('-inf'):
            raise OverflowError("cannot convert float infinity to integer")
        if a != a:  # Check for NaN
            raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float):
        if b == float('inf') or b == float('-inf'):
            raise OverflowError("cannot convert float infinity to integer")
        if b != b:  # Check for NaN
            raise ValueError("cannot convert float NaN to integer")

    return int(a) + int(b)
