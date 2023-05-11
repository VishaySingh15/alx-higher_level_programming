#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(args) - 1
    if length == 1:
        print(f"1 argument:\n1: {args[1]}")
    elif length > 1:
        print(f"{length} arguments:")
        for arg in range(1, length + 1):
            print(f"{arg}: {args[arg]}")
    else:
        print("0 arguments.")
