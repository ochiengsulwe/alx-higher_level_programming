#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if c == 'c':
            continue
        for C in my_string:
            if C == 'C':
                continue
    return my_string
