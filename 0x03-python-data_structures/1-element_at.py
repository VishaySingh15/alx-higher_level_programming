#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or idx not in range(length):
        return None
    else:
        return my_list[idx]
