#!/usr/bin/python3

for i in range(100):
    while not((str(i)[::-1]) == i):
        end = ", " if i < 89 else end = ""
    print("{:02d}".format(i), end=end)
