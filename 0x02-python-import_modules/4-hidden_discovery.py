#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for arg in dir(hidden_4):
        if '__' not in arg:
            print(arg)
