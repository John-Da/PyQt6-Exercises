from pkg_maths.fact import fact
from pkg_maths.fib import fibo

import random

mini = 1
maxi = 4
num = random.randint(mini, maxi)

print(f"fact of {num} is {fact(num)}")
print(f"fib of {num} is {fibo(num)}")