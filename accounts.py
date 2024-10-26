
from transactions import Transaction

class Account:
    def __init__(self, account_number, balance, account_type):
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = []
        self.__account_type = account_type

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @property
    def transactions(self):
        return self.__transactions

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance must be non-negative.")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.__balance += amount
        self.__transactions.append(Transaction(self.__account_number, amount, "deposit"))

    def transfer(self, amount, receiver_account):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount <= self.__balance:
            self.__balance -= amount
            receiver_account.deposit(amount)
            self.__transactions.append(Transaction(self.__account_number, amount, "transfer"))
        else:
            raise ValueError("Not enough funds")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(Transaction(self.__account_number, amount, "withdraw"))
        else:
            raise ValueError("Not enough funds")
