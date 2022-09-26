#!/usr/bin/python3

for i in range(100):
    while ((str(i)[::-1]) != str(i)):
#end = ", " if i < 89 else end = ""
    print("{:02d}".format(i), end=",")
