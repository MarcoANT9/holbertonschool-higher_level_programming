#!/usr/bin/python3
"""
This module returns a list of integers representing the pascal´s triangle
of n.
"""


def pascal_triangle(n):
    """
    This function creates an array of elements representing the Pascal's
    triangle.
    """
    macro = []
    if n < 0:
        return macro
    list_cero = [0]
    list_uno = [1, 1]
    if n >= 0:
        macro.append(list_cero)
    if n >= 1:
        macro.append(list_uno)
    i = 2
    while i < n:
        vector = []
        j = 1
        vector.append(1)
        while j <= i // 2:
            vector.append(macro[i-1][j-1] + macro[i-1][j])
            j += 1
        v_copy = vector[:]
        if i % 2 == 0:
            v_copy.pop()
        v_copy.reverse()
        vector += v_copy
        macro.append(vector)
        i += 1
    return macro

if __name__ == "__main__":
    main()
