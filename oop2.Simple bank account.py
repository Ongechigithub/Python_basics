class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def get_balance(self):
        return f"Account balance for {self.account_holder}: ${self.balance}"

# Creating an instance of the BankAccount class
account1 = BankAccount("Danfelix", 2500)

# Depositing and withdrawing
print(account1.deposit(1000))
print(account1.withdraw(500))

# Checking the balance
print(account1.get_balance())
