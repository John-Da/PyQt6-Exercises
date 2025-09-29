class BankAccount:
    def __init__(self, balane):
        self._balance = balane

    def deposit(self, depositAmount):
        self._balance = self._balance + depositAmount
        print(f"Depositing {depositAmount:.2f}")

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self._balance:
            print("Your Balance is not sufficient to withdraw")
        else:
            self._balance = self._balance - withdrawAmount
            print(f"Withdrawing {withdrawAmount:.2f}")

    def __str__(self):
        return f"The current balance is {self._balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, id, balance, interestRate):
        super().__init__(balance)
        self._id = id
        self._interestRate = interestRate

    def deposit(self, depositAmount):
        self._balance += depositAmount
        print(f"Depositing {depositAmount:.2f}")

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self._balance:
            print("Your Balance is not sufficient to withdraw")
        else:
            self._balance = self._balance - withdrawAmount
            print(f"Withdrawing {withdrawAmount:.2f}")

    def __str__(self):
        return f"The current balance is {self._balance:.2f}"

    def add_interest(self):
        interest = self._balance * self._interestRate
        self.deposit(interest)


savings = SavingsAccount("SA001", 1000, 0.05)
print(f"Initial balance: {savings}")
savings.add_interest()
print(f"After adding interest: {savings}")
savings.deposit(500)
print(f"After depositing money: {savings}")
savings.withdraw(200)
print(f"Final balance: {savings}")
