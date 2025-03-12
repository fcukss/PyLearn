# create class User
# class User:
#    pass
#
#
# #create object of the class User()
# user1 = User()
# user2 = User()
# print(user1)
#
#
# user1.name = "Stas"
# user2.name = "Kate"
# print(user1.name)
# print(user2.name)
#
# user1.name = "Tom"
# print(user1.name)
#
# #delete atribute
# del user2.name
from itertools import count

print("================================================")

class User:
    def __init__(self,n, surname, age=30):
        self.name = n
        self.surname = surname
        self.age = age
        self.money=0

    def greet(self):
        print(f"Hello, {self.name}!")

    def birthday(self):
        self.age +=1

    def add_money(self, n):
        self.money+=n

user1 = User("Stas", "Kaplia")
user2 = User("Kate", "Khoklova", 38)
user3 = User("Tom","Soyer", 16)

print(user1.name, user1.surname, user1.age)   #Stas
print(user2.name, user2.age)

user1.greet()

print(user1.age)    #30
user1.birthday()
print(user1.age)    #31


print(user1.money)   #0
user1.add_money(100)
print(user1.money)   #100







