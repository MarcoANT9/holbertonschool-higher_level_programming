#!/usr/bin/python3
def element_at(my_list, idx):

    '''This program will retrieve an element from a list
       given an index and return it.                 '''

    if idx < 0 or idx >= len(my_list):
        return None

    return my_list[idx]
