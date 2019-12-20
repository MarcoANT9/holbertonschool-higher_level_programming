#!/usr/bin/python3
def best_score(a_dictionary):

    '''This program will get the key with the biggest value and return it.'''

    if not(a_dictionary):
        return None

    keys = a_dictionary.keys()

    max_ = 0

    for keys in a_dictionary:
        if a_dictionary[keys] > max_:
            max_ = a_dictionary[keys]
            name = keys

    return name
