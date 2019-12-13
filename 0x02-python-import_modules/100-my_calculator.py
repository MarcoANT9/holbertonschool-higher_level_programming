#!/usr/bin/python3
def main():

    import sys

    args = len(sys.argv)
    if args != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

        from calculator_1 import add, sub, mul, div

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = str(sys.argv[2])
    op_list = ["+", "-", "*", "/"]

    if not(operator in op_list):
        print("Unknown operator. Available operators: ", end="")
        print("+, -, * and /")
        exit(1)

    if operator == op_list[0]:
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    if operator == op_list[1]:
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    if operator == op_list[2]:
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    if operator == op_list[3]:
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))


if __name__ == "__main__":
    main()
