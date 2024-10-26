
from accounts import Account
from customers import Customer, display_customer_info
from transactions import Transaction


if __name__ == "__main__":
    customer1 = Customer("Anush", "095772299")
    customer2 = Customer("John", "0123456789")
    account1 = Account(12345678910, 1000, "Checking")
    account2 = Account(9876543210, 500, "Savings")
    customer1.add_account(account1)
    customer2.add_account(account2)

    print("Account Balances:")
    display_customer_info(customer1)
    display_customer_info(customer2)
    account1.deposit(200)
    account2.deposit(300)


    print("Deposits:")
    display_customer_info(customer1)
    display_customer_info(customer2)
    account1.withdraw(150)
    account2.withdraw(50)
    print("After Withdrawals:")
    display_customer_info(customer1)
    display_customer_info(customer2)

    account1.transfer(100, account2)

    display_customer_info(customer1)
    display_customer_info(customer2)


    for transaction in account1.transactions:
        print(transaction)

    for transaction in account2.transactions:
        print(transaction)
