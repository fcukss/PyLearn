# class Degree:
#     MIN_DEGREE = 0
#     MAX_DEGREE = 100
#
#     def __init__(self, value):
#         self.value = value
#
#     @classmethod
#     def check_valid_degree(cls, a):
#         print("Класс метод")
#         return cls.MIN_DEGREE <= a <= cls.MAX_DEGREE
#
#     def check_valid_degree1(self):
#         print("Обычный метод класса")
#         return self.MIN_DEGREE <= self.value <= self.MAX_DEGREE
#
#     @staticmethod
#     def check_valid_degree2(value):
#         print("Статик метод")
#         print(Degree.MIN_DEGREE <= value <= Degree.MAX_DEGREE)
#
#     def check(self):
#         print("Отдельная функция")
#         if self.check_valid_degree1():
#             print(True)
#         else:
#             print(False)
#
#
# """
# В целом, @staticmethod и @classmethod в Python служат
# для определения методов, которые не требуют доступа
# к экземпляру класса. Они оба полезны в разных ситуациях,
# и выбор между ними зависит от конкретных потребностей вашего кода.
#
# Если вам нужно работать с классом, а не с его экземпляром,
# используйте @classmethod.
# Eсли вам не нужен доступ ни к классу, ни к его экземплярам,
# используйте @staticmethod.
# """
#
# a = Degree(50)
# # #class method  принадлежит классу
# # a.check_valid_degree(200)
# # #class method может вызыватся без создания обьекта
# # Degree.check_valid_degree(200)
#
# # a.check_valid_degree1()
# # a.check_valid_degree2(300)
# Degree.check_valid_degree2(200)
# # a.check()

# ========================================


# class Transport:
#     def __init__(self, name: str, speed: int, capacity: int, fuel_type: str, transport_honk: str):
#         self.name = name
#         self.speed = speed
#         self.capacity = capacity
#         self.fuel_type = fuel_type
#         self.transport_honk = transport_honk
#
#     def start(self):
#         print(f"{self.name} начинает движение.")
#
#     def stop(self):
#         print(f"{self.name} останавливается.")
#
#     def info(self):
#         print(f"Транспорт: {self.name}.\nСкорость: {self.speed} км/ч.\nВместимость: {self.capacity} чел.\n"
#               f"Тип топлива: {self.fuel_type}")
#
#     def honk(self):
#         print(f"{self.name} сигналит {self.transport_honk}.")
#
#
# class Car(Transport):
#     def __init__(self, speed: int, capacity: int, car_type: str, fuel_type: str,
#                  transport_honk="Бип-бип!!!", name="Машина"):
#         super().__init__(name=name, speed=speed, capacity=capacity, fuel_type=fuel_type,
#                          transport_honk=transport_honk)
#         self.car_type = car_type
#
#     def info(self):
#         super().info()
#         print(f"Тип машины: {self.car_type}")
#
#     def honk(self):
#         print("Перед машиной препятствие на дороге")
#         print(f"{self.name} сигналит {self.transport_honk}.")
#         # super().honk()
#
#
# class Train(Transport):
#     def __init__(self, speed: int, capacity: int, train_type: str, fuel_type: str,
#                  num_wagons: int, route_from: str, route_to: str, transport_honk="Ту-ту!!!",
#                  name="Поезд"):
#         super().__init__(name=name, speed=speed, capacity=capacity, fuel_type=fuel_type,
#                          transport_honk=transport_honk)
#         self.train_type = train_type
#         self.num_wagons = num_wagons
#         self.route_from = route_from
#         self.route_to = route_to
#
#     def info(self):
#         super().info()
#         print(f"Тип поезда: {self.train_type}")
#         print(f"Количество вагонов: {self.num_wagons}")
#
#     def route(self):
#         print(f"{self.name} отправляется по маршруту {self.route_from} - {self.route_to}.")
#
#
# class Ship(Transport):
#     def __init__(
#             self, ship_name: str, speed: int, capacity: int, ship_type : str, fuel_type: str,
#             pier: str, transport_honk="Ту-ду!!!", name="Корабль"
#     ):
#         super().__init__(name=name, speed=speed, capacity=capacity, fuel_type=fuel_type,
#                          transport_honk=transport_honk)
#         self.ship_type = ship_type
#         self.pier = pier
#         self.ship_name = ship_name
#
#     def info(self):
#         super().info()
#         print(f"Тип корабля: {self.ship_type}")
#
#     def set_sail(self):
#         print(f"Корабль {self.ship_name} отчаливает от пристани {self.pier}.")
#
#
# a = Train(speed=120, capacity=4, fuel_type="Бензин", num_wagons=30, route_from="Москва",
#           route_to="Санкт-Петербург", train_type="Пассажирский")
# a.info()
# a.start()
# a.route()
# a.stop()
#
# b = Ship(ship_name="Посейдон", speed=100, capacity=2, ship_type="Лайнер", fuel_type="Дизель",
#          pier="Хельсинки")
# b.info()
# b.start()
# b.set_sail()
# b.stop()
#
# c = Car(car_type="Pickup", name="Chevrolet", speed=180, capacity=5, fuel_type="Бензин", )
# c.info()
# c.start()
# c.honk()
# c.stop()

# ================
# print("=============================INCAPSULATION======================")
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand  # public attribute
#         self.__engine_started = False  # private attribute, prefixed with __
#
#     def start_engine(self):
#         self.__engine_started = True
#         print(f"The engine of {self.brand} is now started.")
#
#     def stop_engine(self):
#         self.__engine_started = False
#         print(f"The engine of {self.brand} is now stopped.")
#
#     def is_engine_started(self):
#         return self.__engine_started
#
#
# # Create an instance
# my_car = Car("Toyota", "Corolla")
# my_car.start_engine()  # Engine is started
#
# print(my_car.is_engine_started())  # Output: True
#
# my_car.__engine_started = False  # This won't change the private attribute
# print(my_car.is_engine_started())  # Output: True (private variable still unchanged)

# # ===========================
# print("===================ABSTRACTION==================================")
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"
#
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
#
#
# # We don't need to know how `make_sound` is implemented; we just use it.
# dog = Dog()
# cat = Cat()
#
# print(dog.make_sound())  # Output: Woof!
# print(cat.make_sound())  # Output: Meow!

# ===========================
# print("=============НАСЛЕДОВАНИЕ (INHERITANCE)================")
#
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def move(self):
#         print(f"{self.brand} is moving.")
#
#
# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)  # Call the parent class constructor
#         self.model = model
#
#     def honk(self):
#         print(f"{self.brand} {self.model} says honk!")
#
#
# # Create an instance of the Car class
# my_car = Car("Toyota", "Corolla")
# my_car.move()  # Inherited method
# my_car.honk()  # Car's own method

# ====================================
# print("==========POLIMORPHIZM==================")
#
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#        return "no sound"
#
#
# class Bird:
#     def make_sound(self):
#         return "Tweet"
#
#
# class Dog:
#     def make_sound(self):
#         return "Bark"
#
#
# def animal_sound(animal):
#     print(animal.make_sound())
#
#
# # Using polymorphism to call the same method on different objects
# bird = Bird()
# dog = Dog()
#
#
#
# animal_sound(bird)  # Output: Tweet
# animal_sound(dog)   # Output: Bark


# ========================================


# class Book:
#     # Class-level attribute
#     book_count = 0
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.book_count += 1
#
#     @classmethod
#     def get_book_count(cls):
#         return f"There are {cls.book_count} books created."
#
#
# # Test classmethod
# book1 = Book("1984", "George Orwell")
# book2 = Book("Brave New World", "Aldous Huxley")
#
# print(Book.get_book_count())  # Output: There are 2 books created.


# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
#
# # Test staticmethod
# print(MathUtils.add(5, 7))       # Output: 12
# print(MathUtils.multiply(3, 4))  # Output: 12
#
# cl = MathUtils()
# print(cl.add(5, 7))
# print(cl.multiply(3, 4))


# ========================================
#
# class Animal:
#     def __init__(self, name: str):
#         self._name = name
#
#     def eat(self):
#         print(f"{self._name} ест")
#
#     def move(self):
#         print(f"{self._name} сидит")
#
#
# class Main:
#     def __init__(self, name: str):
#         pass
#
#
# class Mammal(Animal):
#
#     def __init__(self, name: str):
#         super().__init__(name)
#
#     def move(self):
#         print(f"{self._name} ходит")
#
#
# class Bird(Animal):
#     def __init__(self, name: str):
#         super().__init__(name)
#
#     def move(self):
#         print(f"{self._name} летает")
#
#
# class Bat(Mammal, Bird, Main):
#     def __init__(self, name: str):
#         super().__init__(name)
#
#     def move(self):
#         super().move()
#
#
# a = Bat(name="Бат")
# a.move()


# class Engine:
#     def start(self):
#         print("Engine started")
#
#     def stop(self):
#         print("Engine stopped")
#
#
# class Wheels:
#     def rotate(self):
#         print("Wheels are rotating")
#
#
# class Car(Engine, Wheels):
#     def drive(self):
#         print("The car is driving")
#
#
# my_car = Car()
# my_car.start()  # Inherited from Engine
# my_car.rotate()  # Inherited from Wheels
# my_car.drive()  # Defined in Car class


# class A:
#     def greet(self):
#         print("Hello from A")
#
# class B(A):
#     def greet(self):
#         print("Hello from B")
#
# class C(A):
#     def greet(self):
#         print("Hello from C")
#
# class D(B, C):  # D inherits from both B and C
#     pass
#
# d = D()
# d.greet()  # Which greet method is called: B


# class Engine:
#     def start(self):
#         print("Engine started")
#
#     def stop(self):
#         print("Engine stopped")
#
#
# class Wheels:
#     def rotate(self):
#         print("Wheels are rotating")
#
#
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#         self.wheels = Wheels()
#
#     def drive(self):
#         self.engine.start()
#         self.wheels.rotate()
#         print("The car is driving")
#
#
# car = Car()
# car.drive()

import copy

class Student:

    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = copy.deepcopy(grades)

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)


std = Student("Tom", "riddle")
sstd2 = Student("Harry", "Potter")
std.add_grade([98, 56])
sstd2.add_grade(77)

print(std.grades)
print(sstd2.grades)


# for student in students:
#     print(student.grades)
#     print(student.get_average())
#
# print(studentGrades)