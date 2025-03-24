#===================== Getters ad Setters====
#=========standart getters
# class Student:
#     def __init__(self, name, grade):
#         self._name = name     # Private attribute
#         self._grade = grade   # Private attribute
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if isinstance(name, str):   # Simple validation
#             self._name = name
#         else:
#             raise ValueError("Name must be a string.")
#
#     def get_grade(self):
#         return self._grade
#
#     def set_grade(self, grade):
#         if 0 <= grade <= 100:       # Ensures valid grade
#             self._grade = grade
#         else:
#             raise ValueError("Grade must be between 0 and 100.")
#
# student = Student("Alice", 85)
# print(student.get_name())   # Outputs: Alice
# student.set_grade(90)       # Sets grade to 90
# print(student.get_grade())  # Outputs: 90

#--------------------------------------------------
#getter with usung decorator PRopery start in python 3
#
# class Student:
#     def __init__(self, name, grade):
#         self._name = name
#         self._grade = grade
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def grade(self):
#         return self._grade

#=====setters=============
# class Student:
#     def __init__(self, name, grade):
#         self._name = name
#         self._grade = grade
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         if isinstance(name, str):
#             self._name = name
#         else:
#             raise ValueError("Name must be a string.")
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, grade):
#         if 0 <= grade <= 100:
#             self._grade = grade
#         else:
#             raise ValueError("Grade must be between 0 and 100.")
#
# student = Student("Alice", 85)
# print(student.name)      # Outputs: Alice (getter called)
# student.name = "Bob"     # Setter called to change name to Bob
# print(student.grade)     # Outputs: 85
# student.grade = 95       # Setter called to change grade to 95