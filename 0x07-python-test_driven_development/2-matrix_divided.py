#!/usr/bin/python3

"""
Module contain a function
functions:
    matrix_divided: divide a matrix by int or float
"""


def matrix_divided(matrix, div):
    """
    divide each element in sublist in matrix by div

    Args:
        matrix (list): list of lists
        div (int): divisor

   Returns:
       the list divided
    """
    msg_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(msg_err)
    if not isinstance(matrix, list):
        raise TypeError(msg_err)
    for sub_list in matrix:
        if not isinstance(sub_list, list):
            raise TypeError(msg_err)
        for item in sub_list:
            if not isinstance(item, (int, float)):
                raise TypeError(msg_err)
    length = len(matrix[0])
    if not all(len(sub_list) == length for sub_list in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in sub_list] for sub_list in matrix]
