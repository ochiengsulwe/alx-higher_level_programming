#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)

    if (idx > length - 1) or (idx < 0):
        return my_list
    else:
        new_list =  my_list.pop(idx)
        return new_list.insert(idx, element)
