#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)

    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(length - 1))
        for k in range(1, length):
            print("{}: {}".format(k, argv[k]))
