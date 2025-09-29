import unittest
from prob25_3code import fib, factorial


class TestFibonacciFactorial(unittest.TestCase):
    def setUp(self):
        self.test_numbers = [0, 1, 2, 5, 10]
        self.fib_answers = [0, 1, 1, 5, 55]
        self.factorial_answers = [1, 1, 2, 120, 3628800]

    def test_fact(self):
        fact_list = []
        print(f"Testing factorial with {self.test_numbers}")
        for testnum in self.test_numbers:
            fact = factorial(testnum)
            fact_list.append(fact)
        for i in self.test_numbers:
            print(f"Testing factorial with {i}")
        self.assertEqual(fact_list, self.factorial_answers)

    def test_fibo(self):
        fibo_list = []
        print()
        print(f"Testing fib with {self.test_numbers}")
        for testnum in self.test_numbers:
            fibo = fib(testnum)
            fibo_list.append(fibo)
        for i in self.test_numbers:
            print(f"Testing fib with {i}")
        self.assertEqual(fibo_list, self.fib_answers)


if __name__ == "__main__":
    unittest.main()
