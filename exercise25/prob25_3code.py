

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
