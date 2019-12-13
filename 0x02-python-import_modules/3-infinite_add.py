#!/usr/bin/python3
import sys


def main():

    args = len(sys.argv)
    index = 1
    suma = 0
    while index < args:
        suma += int(sys.argv[index])
        index += 1
    print(suma)

if __name__ == "__main__":
    main()
