#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:

        print("{:d}".format(value))

    except TypeError:
        print("Exception: The value is not compatible with format 'd'",
              file=sys.stderr)
        return False

    return True

if __name__ == "__main__":
    main()
