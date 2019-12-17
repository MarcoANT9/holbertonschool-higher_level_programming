#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    '''Replaces a member in the my_list list at index idx for the
       element introduced in the function. Does nothing on error
       or if the index is out of bounds                       '''

    if idx < 0 and idx >= len(my_list):
        return None

    else:
        my_list[idx] = element
        return my_list
