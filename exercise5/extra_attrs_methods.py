class BankAccount:

    bank_name = "DME KKU Bank"

    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = float(balance)
        self.owner_name = owner_name


    def deposit(self, depositAmount):
        self.balance = self.balance + depositAmount
        print(f'Deposited ${depositAmount}. New balance: ${self.balance}')

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.balance:
            print("Your Balance is not sufficient to withdraw")
        else:
            self.balance = self.balance - withdrawAmount
            print(f'Withdrew ${withdrawAmount}. New balance: ${self.balance}')

    @classmethod
    def from_string(cls, account_string):
        newAccount = account_string.split(',')
        return BankAccount(newAccount[0], newAccount[1], newAccount[2])


print(f"=== Welcome to {BankAccount.bank_name} ===")
account1 = BankAccount("1234567", 1000.0, "Alice")
print(f"Account 1: {account1.owner_name}, Balance: ${account1.balance}")

account1.deposit(500)
account1.withdraw(200)

account2 = BankAccount.from_string("7654321,1500.0,Bob")
print(f"Account 2: {account2.owner_name}, Balance: ${account2.balance}")

