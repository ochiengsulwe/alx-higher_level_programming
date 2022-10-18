#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    my_list

    if (idx < length):
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
    else:
        if (idx < 0) or (idx > length):
            return None


