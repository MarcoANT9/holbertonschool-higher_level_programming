#!/usr/bin/python3
def print_list_integer(my_list=[]):

    ''' This function will print all the integers
        in a given list.                      '''

    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))
