#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    for items in my_list:
        result_list.append(item % 2 == 0)
    return result_list
