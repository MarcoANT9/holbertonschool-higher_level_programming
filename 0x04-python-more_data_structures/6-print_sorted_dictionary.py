#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    '''This function will print a sorted dictionary. '''

    for index in sorted(a_dictionary):
        print(index, end="")
        print(":", a_dictionary[index])
