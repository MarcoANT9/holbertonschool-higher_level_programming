#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    '''This program will multiply all the values on a dictionary by two.'''

    new_dic = {}

    for index in a_dictionary:
        new_dic[index] = a_dictionary.get(index) * 2

    return new_dic
