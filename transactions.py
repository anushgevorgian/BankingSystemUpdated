
class Transaction:
    def __init__(self, account_number, amount, transaction_type):
        self.account_number = account_number
        self.amount = amount
        if transaction_type not in ["deposit", "transfer", "withdraw"]:
            raise ValueError("Invalid transaction type")
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Transaction(account: {self.account_number}, type: {self.transaction_type}, amount: {self.amount})"
