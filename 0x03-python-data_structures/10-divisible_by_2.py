#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    '''This program will search which elements of a list are
       divisible by two, it will return a list containing the
       booleans "True" and "False" according to the division.'''

    bool_list = []

    for index in my_list:
        if index % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)

    return bool_list
