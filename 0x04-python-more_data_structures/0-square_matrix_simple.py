#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for n in range(len(matrix)):
        square = [number**2 for number in matrix[n]]
        new_matrix.append(square)
    return new_matrix
