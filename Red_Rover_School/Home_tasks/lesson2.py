# # task1
# num_1 = 100
# name = "Алексей"
# first_number = 1
# text = "Мой текст"
# mуыsage = "Hi!"
#
# # Task2
# name = "Stas"
# print("Hello my name is", name)
# print(f"Hello my name is {name}")
#
# # #Task3
# # name = input().title()
# # surname = input().title()
# # print(f"Hello, my name is {name} {surname}")
#
# # Task4
# a = input()
# b = input()
# print(int(a) + int(b))
from queue import PriorityQueue

print("------------------------------------------------------------------")

"""Задача 1:
Необходимо ввести 2 числа из консоли, присвоив значения переменным.
Произвести вывод результатов всех произведенных математических действий в консоль.
Виды операций на Ваше усмотрение.
Вывод необходимо производить используя один из трех вариантов форматирования строк.
Пример получившегося вывода: 
"Результатом __операция__ над числами __а__ и __b__ будет __результат__"
(Подсказка: __х__ - необходимые значения)
(Пример вывода: "Результатом сложения над числами 3 и 5 будет 8")"""

import math

# def print_math_op():
#
#     print("Enter to int numbers:")
#     a = int(input())
#     b = int(input())
#     print("Enter math operation (+-*/):")
#     math_op = input()
#     operations = {
#         '+': a+b,
#         '-': a-b,
#         '*': a*b,
#         '/':a/b
#     }
#     if math_op in operations:
#         print(f"Результатом '{math_op}' над числами {a} и {b} будет {operations.get(math_op)})")
#
# print_math_op()

print("-------------------------------------------------")
"""Задача 2:
Необходимо получить слово, предложение и/или отрывок текста из консоли и присвоить их переменной/ым.
Произвести над ним действия и применить методы, изученные на уроках и самостоятельно.
Количество примененных методов и их тип зависят только от вашего воображения и изученного материала."""

print("Enter song name:")
song_name = input()
print("Enter author name:")
author_name = input()
print(f"Song name is '{song_name.lower()}' from author - {author_name.upper()} ")



