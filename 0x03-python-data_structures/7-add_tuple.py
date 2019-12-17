#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    '''This program will take two tuples and sum its first two
       elements, later it will return a tuple containint these
       results.                                            '''

    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            s_tu_a = tuple_a[0], 0
        if len(tuple_a) == 0:
            s_tu_a = 0, 0
    else:
        s_tu_a = tuple_a[0], tuple_a[1]

    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            s_tu_b = tuple_b[0], 0
        if len(tuple_b) == 0:
            s_tu_b = 0, 0
    else:
        s_tu_b = tuple_b[0], tuple_b[1]

    sum_tuple_result = (s_tu_a[0] + s_tu_b[0]), (s_tu_a[1] + s_tu_b[1])
    return sum_tuple_result
