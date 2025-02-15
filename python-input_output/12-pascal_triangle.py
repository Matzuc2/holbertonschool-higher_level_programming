#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
              Each inner list corresponds to a row of the triangle.

    Example:
        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    if n <= 0:
        return []

    p_triangle = [[1]]

    for i in range(1, n):
        prev = p_triangle[-1]
        new = [1]

        for j in range(1, len(prev)):
            new.append(prev[j - 1] + prev[j])

        new.append(1)
        p_triangle.append(new)

    return p_triangle
