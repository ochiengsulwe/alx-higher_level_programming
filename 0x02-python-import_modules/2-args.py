#!/usr/bin/python3
import sys.argv

if __name__ == "__main__":

    length = len(argv)
    
    for k in range(length):
        print("{:d} argument: ".format(length))
        print("{:s}".format(argv[k])
    else:
    if length == 0:
    print("{:d} arguments.".format(length))
    else:
    print("{:d} arguments: ".format(length))
    print("{:d}: {:s}".format(argv.index(argv[k] + 1), argv[k]))

