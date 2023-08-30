#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys


def validate_input(args):
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)


operator_mapping = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


if __name__ == "__main__":
    validate_input(sys.argv)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator in operator_mapping:
        result = operator_mapping[operator](a, b)
        print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
