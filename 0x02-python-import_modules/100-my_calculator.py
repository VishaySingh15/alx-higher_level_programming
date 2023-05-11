#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(args[1])
    b = int(args[3])
    if args[2] == '+':
        result = calc.add(a, b)
    elif args[2] == '-':
        result = calc.sub(a, b)
    elif args[2] == '*':
        result = calc.mul(a, b)
    else:
        result = calc.div(a, b)
    print(f"{a} {args[2]} {b} = {result}")
