#!/usr/bin/python3
import sys


def main():
    args = len(sys.argv) - 1
    print("{}".format(args), end="")
    if args == 0:
        print(" arguments.")
    elif args == 1:
        print(" argument:")
        print("1. {}".format(sys.argv[1]))
    else:
        index = 1
        print(" arguments:")
        while (index < args + 1):
            print("{}: {}".format(index, sys.argv[index]))
            index += 1

if __name__ == "__main__":
    main()
