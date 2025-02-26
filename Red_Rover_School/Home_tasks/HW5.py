print("=============================Task1==================================")

"""
Продвинутый sum.
Встроенная функция sum() в python вызывает ошибку, если один
из элементов последовательности не является числом, например sum([1, 2, ‘A’]).
Напишите функцию sum_ignore_non_numbers(),
которая имеет один параметр items (список или кортеж).
Функция должна вернуть сумму всех чисел (int, float)
в переданной последовательности. При этом все нечисловые значения должны игнорироваться.
Если чисел нет, то функция должна вернуть 0.

Если вызвать функцию со списком [1, 2, 'Hey', None, 4.3], то она должна вернуть 7.3
"""

def sum_ignore_non_numbers(items):
    return sum(i for i in items if isinstance(i, (int,float)))

    # return sum(filter(lambda i: isinstance(i, (int, float)), items))

print(sum_ignore_non_numbers([]))
print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))



print("=============================Task2==================================")

"""

Треугольник.
Треугольник возможен, если сумма любых двух его сторон больше длины третьей стороны.
Напишите функцию is_triangle(), 
которая имеет 3 параметра - длины сторон треугольника. 
Функция должна возвращать True, 
если треугольник с переданными сторонами может существовать, и False в противном случае.

Для is_triangle(2, 4, 9) правильный ответ - False, для is_triangle(3, 4, 5) - True.
"""

def is_triangle(a, b, c):
    if a | b | c == 0:
        return False
    if (a + b > c) and (a + c > b) and (c + b > a):
        return True
    else:
        return False

print(is_triangle(2, 4, 9))
print(is_triangle(3, 4, 5))

print("=============================Task3==================================")

"""
Среднее значение.
Напишите функцию average(), которая принимает 
произвольное количество позиционных аргументов. 
(Можно передать любое число аргументов).
Функция должна посчитать среднее арифметическое 
всех переданных чисел. (Представим, что в функцию передаются только числа).
Если не передать ни одного аргумента, то функция должна вернуть 0.

Такой вызова функции average(1, 2, 3, 4, 5, 6, 7, 8) должен вернуть 4.5
"""

def average(*args):
    if not args:
        return 0
    return sum(args)/len(args)
print(average(1, 2, 3, 4, 5, 6, 7, 8))
print(average())



print("=============================Task4==================================")
"""
Общие строки.
Напишите функцию common_strings(), которая имеет 
3 параметра: list1, list2 и ingore_case=True (значение по умолчанию).
Функция должна вернуть новых список из тех значений, 
которые встречаются в обоих списках. 
При этом, если ignore_case равен True, то функция должна 
игнорировать регистр и считать строки “string” и “STRING” одинаковыми.  
В противном случае функция должна учитывать регистр символов 
и считать такие строки разными.
Все строки в результирующем списке должны быть в нижнем регистре.

Например, существуют 2 списка:
fruits_1 = [‘banana’, ‘APPLE’, ‘watermelon’, ‘cherry’] 
fruits_2 = [‘Mango’, ‘apple’, ‘orange’, ‘cherry’]
То вызов функции common_strings(fruits_1, fruits_2) должен вернуть [‘apple’, ‘cherry’].
"""


def common_strings( list1, list2 , ingore_case=True):
    if  ingore_case:
        set1 = set(map(str.lower, list1))
        set2 = set(map(str.lower, list2))
        # set1 = {word.lower() for word in list1}
        # set2 = {word.lower() for word in list2}
    else:
        set1 = set(list1)
        set2 = set(list2)
    return list(set1.intersection(set2))




fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']

print(common_strings(fruits_1, fruits_2))
print(common_strings(fruits_1, fruits_2,False))


print("===========================Повторение прошлого материала.=================================")
"""
Повторение прошлого материала.


Task1
КаКоЕ-тО вОлНеНиЕ.

Создать переменную text, значение которой определяется через ввод данных с клавиатуры.
Каждый символ под четным индексом должен быть переведен в верхний регистр, а каждый нечетный в нижний.
Вывести полученную строку на экран.

Если была введена строка 
“Чтобы продать что-нибудь ненужное, нужно сначала купить что-нибудь ненужное, а у нас денег нет.”, 
то результат должен быть  
“ЧтОбЫ ПрОдАтЬ ЧтО-НиБуДь нЕнУжНоЕ, нУжНо сНаЧаЛа кУпИтЬ 
ЧтО-НиБуДь нЕнУжНоЕ, а у нАс дЕнЕг нЕт.”
"""

def recase():
    text = input()
    return "".join(c.upper() if i%2==0 else c.lower() for i,c  in enumerate(text))

print(recase())


