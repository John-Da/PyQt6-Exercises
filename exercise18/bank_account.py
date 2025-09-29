class BankAccount:
    # define init method with account_number, owner_name, and initial_balance as parameters

    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.initial_balance = initial_balance

    # define deposit method with amount as parameter

    def deposit(self, depo_amount):
        try:
            if depo_amount > 0:
                self.initial_balance += depo_amount
                return f"Deposited ${depo_amount:.2f}. New balance: ${self.initial_balance:.2f}"
            else:
                return f"Deposit amount must be greater than 0"

        except ValueError:
            return f"Deposit amount must be greater than 0"

        except TypeError:
            return f"Invalid deposit amount"

    # define withdraw method with amount as parameter

    def withdraw(self, withdraw_amount):
        try:
            if withdraw_amount < 0:
                return f"Withdraw amount must be greater than 0"

            if withdraw_amount > self.initial_balance:
                return f"Insufficient funds"

            else:
                self.initial_balance -= withdraw_amount
                return (
                    f"Withdrew ${withdraw_amount:.2f}. New balance: ${self.initial_balance:.2f}"
                )

        except TypeError:
            return f"Invalid withdrawal amount"

    def get_balance(self):
        return self.initial_balance

    def __str__(self):
        return f"Account {self.account_number} owned by {self.owner_name}, Balance: ${self.initial_balance:.2f}"


# Test the BankAccount class
if __name__ == "__main__":
    # Create a new account
    account1 = BankAccount("1234567890", "John Doe", 1000)
    account2 = BankAccount("0123456789", "Manee Jaidee")

    # Print initial account details
    print("Initial account details:")
    print(account1)
    print(account2)

    # Make some deposits
    print("\nMaking deposits:")
    print(account1.deposit(500))
    print(account1.deposit("a"))
    print(account1.deposit(-50))  # Testing invalid deposit

    # Make some withdrawals
    print("\nMaking withdrawals:")
    print(account1.withdraw(200))
    print(account1.withdraw(2000))  # Testing insufficient funds
    print(account1.withdraw("a"))
    print(account1.withdraw(-100))  # Testing invalid withdrawal

    # Get and print the current balance
    print(f"\nCurrent balance: ${account1.get_balance():.2f}")

    # Print final account details
    print("\nFinal account details:")
    print(account1)
    print(account2)
