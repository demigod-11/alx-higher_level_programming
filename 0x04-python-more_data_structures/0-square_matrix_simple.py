#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    length = len(new_matix)
    for row in range(length):
        new_matrix[row] = list(map(lambda x: x ** 2, new_matrix[row]))
    return new_matrix
