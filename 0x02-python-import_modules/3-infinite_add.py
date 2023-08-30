#!/usr/bin/python3

import sys

def calculate_sum(arguments):
    length = len(arguments)
    summ = 0
    if length == 0:
        summ = 0
    else:
        for i in range(length):
            summ += int(arguments[i])
    return summ

if __name__ == "__main__":
    summ = calculate_sum(sys.argv[1:])
    print("{:d}".format(summ))

