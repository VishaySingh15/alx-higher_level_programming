#!/usr/bin/python3
def max_integer(my_list=[]):
    m = my_list[0]
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > m:
            m = i
    return (m)
