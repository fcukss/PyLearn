"""
Представьте, что вам надо сделать банк, в котором будут клиенты, у которых будут счета.
Что можно будет делать в банке:
Добавлять новых клиентов в банк
Находить клиента по номеру паспорта
Добавлять счёт клиенту
Находить счёт клиента по номеру паспорта
Класть/снимать деньги по номеру паспорта
"""


class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, first_name, last_name, passport_number):
        new_customer = Customer(first_name, last_name, passport_number)
        self.customers[passport_number] = new_customer

    def get_customer(self, passport_number):
        if passport_number in self.customers:
            return self.customers[passport_number]
        raise KeyError()

    def add_account(self, account, customer):
        self.accounts[customer] = account

    def get_customer_account(self, passport_number):
        customer = self.get_customer(passport_number)
        if customer not in self.accounts:
            raise KeyError()
        return self.accounts[customer]

    def deposit(self, passport_number, amount):
        bank_account = self.get_customer_account(passport_number)
        bank_account.deposit(amount)

    def withdraw(self, passport_number, amount):
        bank_account = self.get_customer_account(passport_number)
        bank_account.withdraw(amount)


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, money):
        self.amount += money
        return self.amount

    def withdraw(self, money):
        self.amount -= money
        return self.amount


bank = Bank()
bank.add_customer("John", "Dou", "CV453214")
bank.add_customer("Bred", "Pitt ", "BP453214")
bank_account = BankAccount("123456", "USD")
bank_account2 = BankAccount("654123", "USD")
bank.add_account(bank_account, bank.get_customer("CV453214"))
bank.add_account(bank_account2, bank.get_customer("BP453214"))

bank.deposit("CV453214", 100)
bank.deposit("BP453214", 100)
