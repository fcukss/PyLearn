# class User:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'User {self.name} {self.surname}'
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, new_name):
#         if isinstance(new_name,str):
#             self.name = new_name
#
# user = User("Tom", "Smith")
# print(user)
#
#
# name = user.get_name()
# user.set_name("Bill")
#
# print(user)   #User Bill Smith
#==================================================================
# class User:
#     def __init__(self, name, surname):
#         self._name = name
#         self.surname = surname
#
#     @property
#     def name(self):
#         return self._name
#
#
#
#
# user = User("Tom", "Smith")
# print(user.name)
# # user.name = "Bill"
# print(user.name)

#==================================================================
# class User:
#     def __init__(self, name, surname):
#         self.__name = name   #private attribute
#         self.__surname = surname
#
#     def get_name(self):
#         return self.__name
#
#
#
# user = User("Tom", "Smith")
# # print(user.__name)
# print(user.get_name())  #Tom
# user.__name = "Bill"    #неизменяет приватный аттрибут
# print(user.get_name())   #Tom

#==================================================================

#
# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def greet(self):
#         print(self.name)
#
# class ProUser(User):
#     def __init__(self, name, surname, desc, age = None):
#         super().__init__(name,surname,age)
#         self.desc = desc
#
#     def greet(self):
#         print(f"hello {self.name}")
#
#     def show_desc(self):
#         print(self.desc)
#
# # class Admin(User):
# #
# #     def greet(self):
# #         print(f"Admin {self.name}")
# #
#
#
# user = User("Stas", "Kaplia", 37)
# user.greet()
#
# pro_user = ProUser("Jack", "Smith","programm")
# pro_user.greet()
#
# # admin = Admin("Bill")
# # admin.greet()

# pro_user.show_desc()
#==================================================================


