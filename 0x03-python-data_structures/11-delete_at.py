#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    '''This program will delete an integer from a list
       given an index position.                    '''

    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]

    return my_list
