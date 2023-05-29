#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for b in range(x):
        try:
            print(f"{my_list[b]}", end="")
        except Exception:
            return count
        else:
            count += 1
    print()
    return count
