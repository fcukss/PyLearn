"""
==================TASK1==================================
Перенесите ваши функции из прошлого домашнего задания
в отдельный файл и импортируйте их в основной (исполняемый) файл.
Запустите каждую вашу функцию по 1 или более раз в исполняемом файле.
"""
import math
from inspect import stack

# import HW5

# print(HW5.sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))
# print(HW5.is_triangle(3, 4, 5))
# print(HW5.average(1, 2, 3, 4, 5, 6, 7, 8))
#
# fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
# fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
# print(HW5.common_strings(fruits_1, fruits_2))

"""
==========================TASK2===============================
Создайте анонимную функцию pow, которая принимает 2 аргумента x и y. 
Функция должна возвращать x, возведенное в степень y.
"""


res = lambda x,y:pow(x,y)
print(res(2,2))



"""
=============================TASK3===================================
Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
Функция должна создать новую строку, где все гласные буквы aeiouyAEIOUY 
в строке text дублируются.
Например, такой вызовы функции snake_talk(“Harry”) должен вернуть строку “Haaryy”.
"""

# def snake_talk(text):
#     pattern = "aeiouyAEIOUY"
#     res=[]
#     for c in text:
#         if c in pattern:
#             res.append(c*2)
#         else:
#             if c not in res:
#                 res.append(c)
#
#     return ''.join(res)

def snake_talk(text):
    pattern = "aeiouyAEIOUY"
    res=''
    for c in text:
        if c in pattern:
            res+=c
        res+=c
    return res

print(snake_talk("Harry"))


