#====================== Override and overload

# #overriding
# class Animal:
#     def sound(self):
#         return "Some generic animal sound"
#
# class Dog(Animal):
#     # Overriding the parent class method
#     def sound(self):
#         return "Bark"
#
# generic_animal = Animal()
# dog = Dog()
#
# print(generic_animal.sound())  # Output: Some generic animal sound
# print(dog.sound())             # Output: Bark
#
# #overloading
# class Calculator:
#     # def add(self, a, b=0, c=0):
#     #     return a + b + c
#
#     def add(self, *args):
#         return sum(args)
#
#
# calc = Calculator()
# print(calc.add(5))  # Output: 5 (only one argument)
# print(calc.add(5, 10))  # Output: 15 (two arguments)
# print(calc.add(5, 10, 15))  # Output: 30 (three arguments)
#

# ==================  Dispatch decorator

# from functools import singledispatch
#
# @singledispatch
# def process_data(data):
#     print(f"Default processing for {data}")
#
# @process_data.register(int)
# def _(data: int):
#     print(f"Processing integer: {data}")
#
#
# @process_data.register(str)
# def _(data: str):
#     print(f"Processing string: '{data}'")

# process_data(42)  # Output: Processing integer: 42
# process_data("Hi")  # Output: Processing string: 'Hi'
# process_data([1, 2, 3])  # Output: Default processing for [1, 2, 3]

# from multipledispatch import dispatch
#
# @dispatch(int, int)
# def add(a, b):
#     return a + b
#
# @dispatch(str, str)
# def add(a, b):
#     return a + " " + b
#
# @dispatch(list, list)
# def add(a, b):
#     return a + b
#
# print(add(2, 3))  # Output: 5
# print(add("Hello", "World"))  # Output: "Hello World"
# print(add([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]

# from multipledispatch import dispatch
#
# @dispatch(float)
# def area(radius):
#     """Calculate area of a circle"""
#     return 3.14 * radius * radius
#
# @dispatch(float, float)
# def area(length, breadth):
#     """Calculate area of a rectangle"""
#     return length * breadth
#
# print(area(5.0))  # Circle: Output -> 78.5
# print(area(4.0, 6.0))  # Rectangle: Output -> 24.0

# from functools import singledispatchmethod
#
# class Shape:
#     @singledispatchmethod
#     def draw(self, shape):
#         print("Drawing a generic shape")
#
#     @draw.register
#     def _(self, shape: str):
#         print(f"Drawing a string-based shape: {shape}")
#
#     @draw.register
#     def _(self, shape: int):
#         print(f"Drawing a shape with {shape} sides")
#
# s = Shape()
# s.draw("circle")  # Output: Drawing a string-based shape: circle
# s.draw(4)  # Output: Drawing a shape with 4 sides
# s.draw([1, 2])  # Output: Drawing a generic shape
