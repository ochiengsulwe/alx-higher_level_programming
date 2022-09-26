#!/usr/bin/python3

for i in range(100):
    if ((str(i)[::-1]) is not str(i)):
         end = ", " if i < 89 else end = ""
        print("{:02d}".format(i), end=",")
