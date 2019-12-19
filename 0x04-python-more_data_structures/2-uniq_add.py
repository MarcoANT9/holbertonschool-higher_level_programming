#!/usr/bin/python3
def uniq_add(my_list=[]):

    '''This function will sum all the unique elements in a list.'''

    summ = 0
    sumed = []

    for index in my_list:
        if index in sumed:
            continue
        else:
            sumed.append(index)
            summ = summ + index

    return summ
