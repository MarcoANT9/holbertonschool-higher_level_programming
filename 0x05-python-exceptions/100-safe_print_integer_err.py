#!/usr/bin/python3
import sys
def safe_print_integer_err(value):

    try:

        print("{:d}".format(value))

    except (ValueError, TypeError):
        print("Exception: Unknown format code 'd' for object of typr 'str'",
              file=sys.stderr)
        return False

    return True

if __name__ == "__main__":
    main()
