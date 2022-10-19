#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    if (idx > length - 1) or (idx < 0):
        return my_list
    else:
        my_list[idx] = element
        new_list = my_list
        return new_list, my_list
