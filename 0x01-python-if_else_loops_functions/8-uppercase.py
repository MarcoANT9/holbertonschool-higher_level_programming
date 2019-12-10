#!/usr/bin/python3
def uppercase(str):
    """ This function will change any lowercase characters into uppercase"""
    for i in str:
        chara = ord(i)
        if (chara >= 97 and chara <= 133):
            i = i - 32
        print("{:c}". format(chara), end="")
    print()
