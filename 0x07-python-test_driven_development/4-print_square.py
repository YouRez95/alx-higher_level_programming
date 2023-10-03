#!/usr/bin/python3
"""
My module contain one function
Functions:
    print_square: print square
"""


def print_square(size):
    """
    printing a square with #

    Args:
        size (int): size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print('#' * size)
