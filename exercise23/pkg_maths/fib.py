import sys

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 2) + fibo(n - 1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(fibo(int(sys.argv[1])))
