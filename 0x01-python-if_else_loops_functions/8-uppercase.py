#!/usr/bin/python3
def uppercase(str):
    """ This function will change any lowercase characters into uppercase"""
    for i in str:
        i = ord(i)
        if (i in range(97, 133)):
            i = i - 32
        print("{:c}". format(i), end = "")
    print()
