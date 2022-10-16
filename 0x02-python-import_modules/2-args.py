#!/usr/bin/python3
import sys
# a function to list number of arguments in a function
if __name__ == "__main__":
    length = len(sys.argv)

    if length == 0:
	print("{:d} arguments." .format(length - 1))
    elif lenght == 1:
        print("{:d} argument:".format(length - 1))
    else:
        print("{:d} arguments:".format(length - 1))
    for argv in range(1, length):
        print("{:d} : {:s}".format(argv, sys.argv[argv]))
