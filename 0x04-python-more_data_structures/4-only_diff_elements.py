#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    '''This program will return a set of common elements in other two sets.'''

    new_set = set_1 ^ set_2
    return new_set
