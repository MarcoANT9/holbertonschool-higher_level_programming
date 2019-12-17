#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    '''This function will print a matrix of numbers in
       a grid way:
                   a1 a2 a3
                   a4 a5 a6
                   a7 a8 a9
                   ...
       Leaving two dashes and a space at the end.  '''

    if len(matrix[0]) == 0:
        print('')

    else:
        index = 0

        while (index < len(matrix)):
            jndex = 0
            while (jndex < len(matrix[index])):
                print("{:d}".format(matrix[index][jndex]), end="")
                if (jndex + 1 < len(matrix[index])):
                    print(" ", end="")
                else:
                    print("")
                jndex += 1
            index += 1
