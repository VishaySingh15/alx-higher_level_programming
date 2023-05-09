#!/usr/bin/python3
for i in range(96+26, 96, -1):
    num = i
    if i % 2:
        num -= 32
    print("{}".format(chr(num)), end="")
