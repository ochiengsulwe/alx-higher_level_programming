#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        my_string.remove('c')
        for C in my_string:
            my_string.remove('C')
    return my_string
