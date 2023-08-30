#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    val_max = my_list[0]
    for item in my_list:
        if val_max < item:
            val_max = item
    return val_max
