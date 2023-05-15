#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1_l, t2_l = len(tuple_a), len(tuple_b)
    if t1_l == 0:
        t_1 = (0, 0)
    elif t1_l == 1:
        t_1 = (tuple_a[0], 0)
    else:
        t_1 = (tuple_a[0], tuple_a[1])
    if t2_l == 0:
        t_2 = (0, 0)
    elif t2_l == 1:
        t_2 = (tuple_b[0], 0)
    else:
        t_2 = (tuple_b[0], tuple_b[1])
    t_add = t_1[0] + t_2[0], t_1[1] + t_2[1]
    return t_add
