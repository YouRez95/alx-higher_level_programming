#!/usr/bin/python3
"""
This is a module contain a function
Functions:
    add : add two integers
"""


def add_integer(a, b=98):
    """
    Add two numbers and returns the result

    Args:
        a (int): The first number
        bb (int): The second number

    Returns:
        int: the addition of a and b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a + b)
