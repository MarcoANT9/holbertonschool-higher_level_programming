#!/usr/bin/python3
def max_integer(my_list=[]):

    '''This function will find the biggest integer of a list. '''

    if len(my_list) == 0:
        return None

    max_ = my_list[0]

    for index in my_list:
        if index > max_:
            max_ = index

    return max_
