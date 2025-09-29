import sys


def run_calculation(op, b, c):
    try:
        fnum = float(b)
        lnum = float(c)
        if op == "+":
            return f"{fnum:.1f} {op} {lnum:.1f} is {(fnum + lnum):.1f}"
        if op == "-":
            return f"{fnum:.1f} {op} {lnum:.1f} is {(fnum - lnum):.1f}"
        if op == "*" or op == 'x':
            return f"{fnum:.1f} {op} {lnum:.1f} is {(fnum * lnum):.1f}"
        if op == "/":
            return f"{fnum:.1f} {op} {lnum:.1f} is {(fnum / lnum):.1f}"

    except ValueError:
        return "Operands are invalid. They are not numbers"

    except ZeroDivisionError:
        return f"{fnum:.1f} cannot be divided by {lnum:.1f}"


if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Usage:python3 prob25_2.py <operator> <operand1> <operand2>")
    else:
        print(run_calculation(sys.argv[1], sys.argv[2], sys.argv[3]))
