#!/usr/bin/python3
def weight_average(my_list=[]):

    if not(my_list):
        return 0

    sum = 0
    div = 0
    index = 0
    while index < len(my_list):
        sum += (my_list[index][0] * my_list[index][1])
        div += my_list[index][1]
        index += 1

    return sum / div
