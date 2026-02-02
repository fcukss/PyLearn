class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, money):
        self.amount = self.amount + money

    def withdraw(self, money):
        try:
            if self.amount >= money:
                self.amount = self.amount - money
            raise ValueError
        except ValueError:
            "Недостаточно денег на счету"

    def print_account(self):
        print(f'Account number: {self.number}\nAmount: {self.amount} {self.currency}')


account = BankAccount(12345, 'USD')
account.print_account()
account.deposit(100)
account.print_account()
account.withdraw(150)
account.print_account()
