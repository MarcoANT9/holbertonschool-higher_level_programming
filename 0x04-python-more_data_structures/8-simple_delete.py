#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):

    '''This program will delete an element from a dictionary if it exist,
       if it doesn't exist, the original dictionary will remain intact'''

    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
