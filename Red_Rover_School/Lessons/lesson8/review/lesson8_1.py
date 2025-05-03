# ======================  Magic (Dunder) methods

#class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         # !r = неизменяемая часть
#         return f"Person({self.name!r}, {self.age!r})"
#
#     def __str__(self):
#         return f"Person({self.name!r}, {self.age!r})"
#
# person = Person("John", 25)
# print(repr(person))
# print(person)
#
# #==============methods operators======
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"({self.x},{self.y})"
#
# v1 = Vector(2,5)
# v2 = Vector(3, 7)
# v3= v1+v2
# print(v3)   #(5,12)

# ===============================================
# class Person:
#     def __init__(self,name, age):
#             self.name = name
#             self.age = age
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
# p1 = Person("John", 25)
# p2 = Person("John", 25)
# print(p1 == p2)  #True  без eq метода будет False
#
#================================================

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def __str__(self):
#         return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
#
#     def __add__(self, amount):
#         self.balance += amount
#         return self
#
#     def __sub__(self, amount):
#         self.balance -= amount
#         return self
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __gt__(self, other):
#         return self.balance > other.balance
#
# account1 = BankAccount("Alice", 100)
# account2 = BankAccount("Bob", 100)
#
# print(account1)  # Output: Account owner: Alice, Account balance: $100
# account1 + 50  # Deposit
# print(account1)  # Output: Account owner: Alice, Account balance: $150
# account1 - 30  # Withdrawal
# print(account1)  # Output: Account owner: Alice, Account balance: $120
# print(account1 == account2)  # Output: False
# print(account1.__gt__(account2))

#========================= Access Modifiers=====

# #===public methods====
# class Student:
#     def __init__(self, name, age):
#         self.name = name  # Public attribute
#         self.age = age    # Public attribute
#
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
# student = Student("John", 21)
# print(student.name)  # Accessing public attribute
# student.display()    # Accessing public method

#===protected methods====
# class Student:
#     def __init__(self, name, age):
#         self._name = name  # Protected attribute
#         self._age = age    # Protected attribute
#
#
#     def _display(self):  # Protected method
#         print(f"Name: {self._name}, Age: {self._age}")
#
# class GraduateStudent(Student):
#     def show_details(self):
#         print(f"Graduate Student: {self._name}, Age: {self._age}")
#         # Accessing protected members from subclass
#
# # Accessing protected members
# grad_student = GraduateStudent("Jane", 24)
# grad_student.show_details()  # Accessible from subclass
# print(grad_student._name)


# #===private methods====
# class Student:
#     def __init__(self, name, age):
#         self.__name = name  # Private attribute
#         self.__age = age    # Private attribute
#
#     def __display(self):  # Private method
#         print(f"Name: {self.__name}, Age: {self.__age}")
#
#     def access_private(self):
#         self.__display()  # Accessing private method within the class
#
# student = Student("Alice", 22)
# # print(student.__name)  # This will raise an error
# student.access_private()  # Works since it's accessed within the class


# class Student:
#     def __init__(self, name, age):
#         self.name = name  # Public
#         self.age = age  # Public
#         self._school = "ABC School"  # Protected
#         self.__grades = "A+"  # Private
#
#     def display_public(self):
#         print(f"Student Name: {self.name}")
#
#     def _display_protected(self):
#         print(f"School: {self._school}")
#
#     def __display_private(self):
#         print(f"Grades: {self.__grades}")
#
#     def show_all(self):
#         self.display_public()  # Accessing public method
#         self._display_protected()  # Accessing protected method
#         self.__display_private()  # Accessing private method
#
#     # @property
#     # def school(self):
#     #     return self._school
#
# student = Student("Mark", 20)
#
# # print(student.name)
# # student.display_public()
#
# print(student._school)
# # print(student.school)
# student._display_protected()
#
# # print(student.__grades)  # Raises AttributeError
# # student.__display_private()  # Raises AttributeError
#
# # student.show_all()
