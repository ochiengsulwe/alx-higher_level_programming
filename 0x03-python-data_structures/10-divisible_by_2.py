#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    for item in my_list:
        result = item % 2 == 0
        if result:
            result_list.append(True)
            print(f"{item} is divisible by 2")
        else:
            result_list.append(False)
            print(f"{item} is not divisible by 2")
    return result_list
