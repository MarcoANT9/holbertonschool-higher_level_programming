#!/usr/bin/python3
def no_c(my_string):

    '''This function will take out all the 'c' and 'C' characters
       in a string.                                           '''

    new_string = ""

    for i in my_string:
        if i == "c" or i == "C":
            new_string += ""
        else:
            new_string += i

    return new_string
