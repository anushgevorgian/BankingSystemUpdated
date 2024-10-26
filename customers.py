
class Customer:
    def __init__(self, name, contact_information):
        self.__name = name
        self.__contact_information = contact_information
        self.__accounts = []

    @property
    def name(self):
        return self.__name

    @property
    def contact_information(self):
        return self.__contact_information

    def add_account(self, account):
        self.__accounts.append(account)

    def show_accounts(self):
        return [f"{acc.account_number}: {acc.balance}" for acc in self.__accounts]

def display_customer_info(customer):
    print(f"Customer Name: {customer.name}, Contact: {customer.contact_information}")
    accounts = customer.show_accounts()
    if accounts:
        print("Accounts:")
        for account in accounts:
            print(f" - {account}")
    else:
        print("No accounts found.")
    print()