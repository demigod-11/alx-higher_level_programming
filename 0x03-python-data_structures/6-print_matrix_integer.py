#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for i in matrix:
            for j in row:
                print("{:d}".format(j), end=" "
                      if j != i[-1] else '\n')
    else:
        print()
