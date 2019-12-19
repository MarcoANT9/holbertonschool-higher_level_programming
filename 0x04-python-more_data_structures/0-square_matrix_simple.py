#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    '''This function will compute the square root of all integers in
       a matrix.                                                 '''

    new_matrix = []

    for index in matrix:
        jndex = 0
        new_row = []
        while jndex < len(index):
            new_row.append(index[jndex] ** 2)
            jndex += 1
        new_matrix.append(new_row)
    return new_matrix
