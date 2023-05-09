#!/usr/bin/python3
for i in range(1, 100):
    if (i == 89):
        print("{:02d}".format(i))
    if (int(str(i)[::-1]) > i or i < 10):
        print("{:02d}".format(i), end=", ")
