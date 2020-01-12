#!/usr/bin/python3
"""
This is the "matrix_divied" module. Usage: matrix_divided(matrix, div)
>>> matrix_divided([[2, 4, 6], [10, 12, 14]], 2)
[[1, 2, 3], [5, 6, 7]]
"""

def matrix_divided(matrix, div):
    """
    Returns a new matrix with the quotients of the division.
    """

    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have thesame size"

    new_matrix = []
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) == list:
        if type(matrix[0]) != list:
            raise TypeError(error1)
        else:
            len_size = len(matrix[0])

        for i in matrix:
            new_row = []
            len_row = len(i)
            if len_row != len_size:
                raise TypeError(error2)
            if type(i) == list:
                for j in i:
                    if type(j) == int or type(j) == float:
                        new_row.append(j / div)
                    else:
                        raise TypeError(error1)
                new_matrix.append(new_row)
            else:
                raise TypeError(error1)
    else:
        raise TypeError(error1)


    return new_matrix
