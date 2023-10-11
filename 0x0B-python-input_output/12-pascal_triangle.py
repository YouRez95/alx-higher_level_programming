#!/usr/bin/python3
""" module """


def pascal_triangle(n):
    """ pascal triangle """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    else:
        prev_pascal = pascal_triangle(n - 1)
        row = [1]
        for i in range(1, n-1):
            row.append(prev_pascal[n - 2][i - 1] + prev_pascal[n - 2][i])
        row.append(1)
        prev_pascal.append(row)
        return prev_pascal
