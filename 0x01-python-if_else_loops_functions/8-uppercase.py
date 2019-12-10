#!/usr/bin/python3
def uppercase(str):

    for i in str:
        chara = ord(i)
        if (chara >= 97 and chara <= 122):
            chara = chara - 32
        print("{:c}".format(chara), end="")
    print()
