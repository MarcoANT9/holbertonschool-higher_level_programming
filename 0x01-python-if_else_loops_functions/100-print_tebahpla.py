#!/usr/bin/python3
upper = 1
for i in range(122, 96, -1):
    j = i
    if upper % 2 == 0:
        j = j - 32
    print("{:c}".format(j), end="")
    upper += 1
