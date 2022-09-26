#!/usr/bin/python3

for i in range(100):
    end = ", " if i < 89 else " "
    if ((str(i)[::-1]) is not str(i)):
        print("{:02d}".format(i), end=end)
