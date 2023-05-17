#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = []
    for k in list(a_dictionary):
        a.append((k, a_dictionary[k] * 2))
    return dict(a)
