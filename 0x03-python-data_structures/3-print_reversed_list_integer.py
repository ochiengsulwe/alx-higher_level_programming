#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    length = len(my_list)

    if length < 0:
        return "None"
    else:
        for i in my_list:
            print("{:d}".format(i))
