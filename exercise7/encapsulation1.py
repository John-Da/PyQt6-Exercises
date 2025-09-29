class BankAccount:
    def __init__(self, balane):
        self.__balance = balane

    def deposit(self, depositAmount):
        self.__balance = self.__balance + depositAmount
        print(f"Depositing {depositAmount:.2f}")

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.__balance:
            print("Your Balance is not sufficient to withdraw")
        else:
            self.__balance = self.__balance - withdrawAmount
            print(f"Withdrawing {withdrawAmount:.2f}")

    def __str__(self):
        return f"The current balance is {self.__balance:.2f}"


account = BankAccount(1000)
print(account)
account.deposit(500)
print(account)
account.withdraw(200)
print(account)
