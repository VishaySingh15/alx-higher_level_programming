#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for ch in str:
        if ord(ch) in range(97, 97+26):
            upper += chr(ord(ch) - 32)
            continue
        upper += ch
    print("{}".format(upper))
