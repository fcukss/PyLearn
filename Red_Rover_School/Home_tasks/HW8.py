"""
TASK1
"""

class BankAccount:
    def __init__(self, name: str, balance: int):
        self._name = name
        self._balance = balance

    def deposit(self, amount: int):
        self._balance += amount


    def withdraw(self, amount: int):
        if self.get_balance()<=0:
            print("Недостаточно средств!")
        else:
            self._balance -= amount


    def get_balance(self):
        return self._balance


account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance())  # 1500


"""
TASK2
"""

class OverdraftAccount(BankAccount):

    def withdraw(self, amount: int):
        if self.get_balance()<=0:
            self._balance-=amount


jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance()) # -300


"""
TASK3
"""

users = [
    {'id': 345324, 'name': 'Alice', 'age': 25},
    {'id': 1232, 'name': 123, 'age': 30},
    {'id': 7854, 'name': 'Bob', 'age': 22},
    {'id': 33412, 'name': None, 'age': 35},
    {'id': 78845, 'name': 'Charlie', 'age': 28},
    {'id': 45325, 'name': 'Eve', 'age': 40},
    {'id': 745633, 'name': True, 'age': 19},
    {'id': 64364, 'name': 'Frank', 'age': 33}
]

ids=[]
for user in users:
    if not isinstance(user['name'], str):
       ids.append(user['id'])

print(ids)