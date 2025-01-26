#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a valid list of lists of integers/floats,
                   or if div is not a number.
        TypeError: If the rows of the matrix are not of the same size.
        ZeroDivisionError: If div is 0.
    """

    # Check if matrix is a list of lists and is not empty
    if not isinstance(matrix, list) or len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure matrix is not empty and no row is empty
    if any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all elements are int/float and detect NaN or Inf values
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)) or num != num or num == float('inf') or num == -float('inf'):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a valid number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]

#This has been honestly completed by the help of an AI. I couldn't figure
#  all the possibilities for the tests