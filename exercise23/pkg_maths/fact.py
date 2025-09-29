import sys


def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))