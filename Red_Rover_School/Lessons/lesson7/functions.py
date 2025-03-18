# class User:
#     # принадлежит всем экземплярам
#     count = 0
#
#     def __init__(self, n, surname, age=30):
#         self.name = n
#         self.surname = surname
#         self.age = age
#         self.money = 0
#         User.add_count()
#
#
#     def greet(self):
#         print(f"Hello, {self.name}!")
#
#     def birthday(self):
#         self.age += 1
#
#     def add_money(self, n):
#         self.money += n
#
#     #cls - сам класс
#     @classmethod
#     def add_count(cls):
#         cls.count += 1
#
#     @staticmethod
#     def is_valid_age(age):
#         return age > 0
