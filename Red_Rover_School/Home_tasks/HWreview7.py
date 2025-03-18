# =================Color Ghost=========================================

# import random
#
# class Ghost(object):
#     colors = ['red', 'white', "yellow", "purple"]
#     def __init__(self):
#         self.color = random.choice(Ghost.colors)
#
#
# ghost = Ghost()
# print(ghost.color)


# =========================OOP: Object Oriented Piracy========================

# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#
#
#     def is_worth_it(self):
#         crew_weight = self.crew*1.5
#         if self.draft-crew_weight>20:
#             return True
#         else:
#             return False
#
# titanic = Ship(15,10)
# print(titanic.is_worth_it())


# # ============================Building Spheres====================================
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
#         res = self.mass /float(self.get_volume())
#         return float(format(res, '.5f'))
#
#
# ball = Sphere(2, 50)
# print(ball.get_radius())
# print(ball.get_mass())
# print(ball.get_volume())
# print(ball.get_surface_area())
# print(ball.get_density())



#====================Building blocks=========================

class Block:
    # Good Luck!