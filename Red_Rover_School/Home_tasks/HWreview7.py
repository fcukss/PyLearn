# # =================Color Ghost=========================================
#
# import random
#
#
# class Ghost(object):
#     colors = ['red', 'white', "yellow", "purple"]
#
#     def __init__(self):
#         self.color = random.choice(Ghost.colors)
#
#
# ghost = Ghost()
# print(ghost.color)
#
#
# # =========================OOP: Object Oriented Piracy========================
#
# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#
#     def is_worth_it(self):
#         crew_weight = self.crew * 1.5
#         if self.draft - crew_weight > 20:
#             return True
#         else:
#             return False
#
#
# titanic = Ship(15, 10)
# print(titanic.is_worth_it())
#
# # # ============================Building Spheres====================================
# from math import pi
#
#
# class Sphere(object):
#     def __init__(self, radius: float, mass: float):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         res = (4 / 3) * pi * self.radius ** 3
#         return float(format(res, '.5f'))
#
#     def get_surface_area(self):
#         res = 4 * pi * self.radius ** 2
#         return float(format(res, '.5f'))
#
#     def get_density(self):
#         res = self.mass / float(self.get_volume())
#         return float(format(res, '.5f'))
#
#
# ball = Sphere(2, 50)
# print(ball.get_radius())
# print(ball.get_mass())
# print(ball.get_volume())
# print(ball.get_surface_area())
# print(ball.get_density())
#
#
# # ====================Building blocks=========================
# #
# class Block:
#     def __init__(self, parameters=None):
#         self.parameters = list(parameters)
#
#     def get_width(self):
#         return self.parameters[0]
#
#     def get_length(self):
#         return self.parameters[1]
#
#     def get_height(self):
#         return self.parameters[2]
#
#     def get_volume(self):
#         return self.get_width() * self.get_height() * self.get_length()
#
#     def get_surface_area(self):
#         ab = self.get_width() * self.get_length()
#         ac = self.get_width() * self.get_height()
#         bc = self.get_length() * self.get_height()
#         return 2 * (ab + ac + bc)
#
#
# # ===============================Double value every next call ===============================
# class Class:
#     count = 1
#
#     @staticmethod
#     def get_number():
#         res = Class.count
#         Class.count += Class.count
#         return res
#
#
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
#
#
# # ===============================Thinkful - Object Drills: Quarks =========================
#
# class Quark(object):
#     colors = ("red", "blue", "green")
#     flavors = ('up', 'down', 'strange', 'charm', 'top', 'bottom')
#
#     def __init__(self, color, flavor):
#         self.baryon_number = 1 / 3
#         if color in Quark.colors:
#             self.color = color
#         if flavor in Quark.flavors:
#             self.flavor = flavor
#         else:
#             print("Error")
#
#     def interact(self, quark):
#         self.color, quark.color = quark.color, self.color,
#
#
# q1 = Quark('red', 'up')
# print(q1.color)
# print(q1.flavour)
# q2 = Quark("blue", "strange")
#
# q1.interact(q2)
# print(q1.color)
# print(q2.color)
#
#
# #
# #
# # #====================================Refactored Greeting=======================================
# # # TODO: This method needs to be called multiple times for the same person (my_name).
# # # It would be nice if we didn't have to always pass in my_name every time we needed to great someone.
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self, your_name):
#         return "Hello %s, my name is %s" % (your_name, self.name)
#
#
# # ====================================RCompetitive eating scoreboard=======================================
#
# def scoreboard(who_ate_what):
#     res = []
#     for dic in who_ate_what:
#         score = 0
#         for i in dic:
#             match i:
#                 case 'chickenwings':
#                     score += dic['chickenwings'] * 5
#                 case 'hamburgers':
#                     score += dic['hamburgers'] * 3
#                 case 'hotdogs':
#                     score += dic['hotdogs'] * 2
#
#         res.append({'name': dic['name'], 'score': score})
#     # Сортируем результаты: сначала по убыванию баллов, затем по имени
#     return sorted(res, key=lambda x: (-x['score'], x['name']))
#
#
# lst = [{'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
#        {'name': "Big Bob", "chickenwings": 20, 'hamburgers': 4, 'hotdogs': 11}]
#
# print(scoreboard(lst))
#
#
# # ==============================Person Class Bug=================================
# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = f"{self.first_name} {self.last_name}"
#
#
# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)
#
#
# # ========================First-Class Function Factory==========================
# def factory(x):
#     def func(array):
#         return list(map(lambda y: y * x, array))
#
#     return func
#
#
# fives = factory(5)
# my_array = [1, 2, 3]
# res = fives(my_array)
# print(res)

# ===============================Yoga Class=========================================
def yoga(classroom, poses):
    pass

# ==================================Menu Display=========================================
# class Menu:
#     new_arr=[]
#     def __init__(self, array):
#         for i in array:
#             if i== array[0]:
#                 self.new_arr.append([i])
#             else:
#                 self.new_arr.append(i)
#
#     def to_the_right(self):
#             for i in self.new_arr:
#                 if not isinstance(i,list):
#                     i = [i]
#
#     def to_the_left(self):
#         pass
#          # write code here!
#
#     def display(self):
#         print(self.new_arr)
#
#
# menu = Menu([1, 2, 3])
# print(menu.display())
# menu.to_the_right()
# print(menu.display())
# menu.to_the_right()
# print(menu.display())
# menu.to_the_left()
# print(menu.display())
# menu.to_the_left()
# print(menu.display())


#===============Python's Dynamic Classes #1===========
class MyClass:
    pass


def class_name_changer(cls, new_name):
    if not new_name:
        cls.__name__= cls.__name__
    if not new_name[0].isupper():
        cls.__name__ = new_name.title()
    else:
        cls.__name__ = new_name



myObject = MyClass()

class_name_changer(myObject, "svgsd")
print(myObject.__name__)