#!/usr/bin/python3
def weight_average(my_list=[]):
    length = len(my_list)
    if length == 0:
        return 0
    sum_div = 0
    sum_tup = 0
    for tup in my_list:
        l = len(tup)
        sum_div += tup[l - 1]
        mult = 1
        for val in tup:
            mult *= val
        sum_tup += mult
    return sum_tup /sum_div
