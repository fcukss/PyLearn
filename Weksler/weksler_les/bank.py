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


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, money):
        self.amount = self.amount + money

    def withdraw(self, money):
        if money > self.amount:
            raise ValueError("Insufficient funds")
        self.amount = self.amount - money

    def print_balance(self):
        return f"money on account number {self.number} = {self.amount}"


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers[passport_number] = customer

    def add_account(self, account: BankAccount, customer: Customer):
        self.accounts[customer] = account

    def get_customer(self, passport_number):
        if passport_number in self.customers:
            return self.customers[passport_number]
        raise KeyError("Сначала зарегистрируйте клиента!")

    def get_customer_account(self, passport_number):
        customer = self.get_customer(passport_number)
        return self.accounts[customer]

    def deposit(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.deposit(amount)

    def withdraw(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.withdraw(amount)

    def transfer(self, from_passport, to_passport, amount):
        # 1. Получаем оба аккаунта
        acc_from = self.get_customer_account(from_passport)
        acc_to = self.get_customer_account(to_passport)
        # 2. Пробуем снять деньги (тут сработает твоя проверка из п.2)
        acc_from.withdraw(amount)
        # 3. Если снятие прошло успешно, добавляем другому
        acc_to.deposit(amount)



# bank = Bank()
# bank.add_customer('Tom', 'Raddle', 'FL342312')
# bank.add_customer('Harry', 'Poter', 'KJ224223')
# account = BankAccount('12345', 'USD')
# account2 = BankAccount('54321', 'Euro')
# bank.add_account(account, bank.get_customer('FL342312'))
# bank.add_account(account2, bank.get_customer('KJ224223'))
# bank.deposit('FL342312', 100)
# bank.deposit('KJ224223', 100)
#
# bank.transfer('FL342312','KJ224223', 50)
#
# print(account2.print_balance())
# print(account.print_balance())