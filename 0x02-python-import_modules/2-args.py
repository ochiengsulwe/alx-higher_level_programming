#!/usr/bin/python3
from sys import argv
# a function to list number of arguments in a function
if __name__ == "__main__":
    length = len(argv)

    if length == 1:
        print("{:d} argument: ".format(length))
    print("{:s}".format(argv))
    else:
        if length == 0:
	print("{:d} arguments. ".format(length))
	else:
	for k in range(length):
	print("{:d} arguments: ".format(length))
        print("{:d} : {:s} ".format(argv.index[k], argv[k]))
