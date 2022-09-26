#!/usr/bin/python3

for x in range(100):
    end = ", " if x < 99 else " "
    print("{:02d}".format(x), end=end)
