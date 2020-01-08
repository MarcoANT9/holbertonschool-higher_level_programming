#!/usr/bin/python3
def raise_exception_msg(message=""):

    try:
        raise NameError

    finally:
        print(message, end="")
if __name__ == "__main__":
    main()
