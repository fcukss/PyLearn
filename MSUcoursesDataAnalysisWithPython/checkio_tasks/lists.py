# """
# Твоє завдання тут, це створити функцію, що приймає кортеж
# і повертає кортеж лише з 3 елементами - першим,
# третім елементами від початку і другим елементом
# від кінця вхідного кортежу.
#
# """
#
#
# def easy_unpack(elements: tuple) -> tuple:
#     return (elements[0], elements[2], elements[-2])
#
#
# print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
#
# # These "asserts" are used for self-checking
# assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
# assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
# assert easy_unpack((6, 3, 7)) == (6, 7, 3)
# print("___________________________________")
# """
# Ми маємо список логічних (булевих) значень. Давай перевіримо,
# чи більшість елементів є True.
#
# Деякі випадки, варті згадки: 1) порожній список повинен повертати False; 2)
# якщо однакова кількість True і False, функція повинна повертати False.
# """
#
#
# def is_majority(items: list[bool]) -> bool:
#     if not items:
#         return False
#     true_count = sum(items)
#     return true_count > len(items) / 2
#
#
# print(is_majority([True, False, False, True, False]))
# #
# # # These "asserts" are used for self-checking
# # assert is_majority([True, True, False, True, False]) == True
# # assert is_majority([True, True, False]) == True
# # assert is_majority([True, True, False, False]) == False
# # assert is_majority([True, True, False, False, False]) == False
# # assert is_majority([False]) == False
# # assert is_majority([True]) == True
# # assert is_majority([]) == False
#
# print("___________________________________")
#
# """Надано масив з позитивними числами і число N.
# Ви повинні знайти N-ну ступінь елемента в масиві з індексом N.
# Якщо N за межами масива, тодi повернути -1.
# """
#
#
# def index_power(ar: list[int], n: int) -> int:
#     if n >= len(ar):
#         return -1
#     else:
#         return ar[n] ** n
#
#
# print(index_power([1, 2, 3], 2))
#
# # These "asserts" are used for self-checking
# assert index_power([1, 2, 3, 4], 2) == 9
# assert index_power([1, 3, 10, 100], 3) == 1000000
# assert index_power([0, 1], 0) == 1
# assert index_power([1, 2], 3) == -1
# assert index_power([96, 92, 94], 3) == -1
#
# print("___________________________________")
# """
# Задано масив цілих чисел. Потрібно знайти суму елементів
# з парними індексами (0-й, 2-й, 4-й і т.д.),
# а потім перемножити цю суму і останній елемент вихідного масиву.
# """
#
#
# def checkio(array: list[int]) -> int:
#     sum = 0
#     if not array:
#         return 0
#     for i in range(0, len(array), 2):
#         sum += array[i]
#     return sum * array[-1]
#
#
# print(checkio([0, 1, 2, 3, 4, 5]))
#
# # These "asserts" are used for self-checking
# assert checkio([0, 1, 2, 3, 4, 5]) == 30
# assert checkio([1, 3, 5]) == 30
# assert checkio([6]) == 36
# assert checkio([]) == 0
# print("___________________________________")
# """
# Медиана – это числовое значение, которое позволяет разделить
#  отсортированные списки чисел на большее
#  и меньшее количество половинок. В отсортированном списке
#  по разным числам элементов медиана
#  – это число в серединном списке. Для разговора
#  с парными числами элементов, де немає одного элемента
#  точно посередини, медиана – это среднее значение двух чисел,
#  которые находятся в середини списку.
#  В этих задачах непустой список естественных чисел.
#  Вам необходимо узнать медиану даного списку.
#
#
# """
#
#
# def checkio(data: list[int]) -> int | float:
#     data.sort()
#     mediana = len(data) // 2
#     if len(data) % 2 != 0:
#         return data[mediana]
#     else:
#         return (data[mediana] + data[mediana - 1]) / 2
#
#
# print(checkio([1, 2, 3, 4, 5]))
#
# # These "asserts" are used for self-checking
# assert checkio([1, 2, 3, 4, 5]) == 3
# assert checkio([3, 1, 2, 5, 3]) == 3
# assert checkio([1, 300, 2, 200, 1]) == 2
# assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
# assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
# assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
# assert checkio([33, 56, 62]) == 56
# assert checkio([21, 56, 84, 82, 52, 9]) == 54
# assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
# assert checkio([64, 6, 92, 7, 70, 5]) == 35.5
#
# print("__________________________________________")
#
#
# def left_join(phrases: tuple[str, ...]) -> str:
#     res = ""
#     for item in phrases:
#         if item.__contains__("right"):
#             res += item.replace("right", "left") + ","
#         else:
#             res += item + ","
#     return res.strip(',')
#
#
# print("Example:")
# print(left_join(("left", "right", "left", "stop")))
#
# # These "asserts" are used for self-checking
# assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
# assert left_join(("brightness wright",)) == "bleftness wleft"
# assert left_join(("enough", "jokes")) == "enough,jokes"
#
# print("__________________________________________")
#
# """
# У цій місії тобі потрібно слідувати даному переліку інструкцій,
# які приведуть тебе до певної точки на мапі.
# Цей перелік у вигляді рядка, кожна літера
# якого вказує на напрямок твого наступного кроку.
#
# Буква "f" - каже тобі йти вперед,
#     "b" - назад,
#     "l" - ліворуч
#     "r" - праворуч.
#
# Це означає, що якщо список твоїх інструкцій наступний - "fflff",
# то тобі слід йти вперед два кроки,
# зробити один крок ліворуч і потім знову двічі вперед.
# """
#
#
# def follow(commands: str) -> tuple[int, int] | list[int]:
#     # Начальная позиция
#     x, y = 0, 0
#
#     # Словарь направлений
#     directions = {
#         'f': (0, 1),  # Вперёд
#         'b': (0, -1),  # Назад
#         'l': (-1, 0),  # Влево
#         'r': (1, 0)  # Вправо
#     }
#
#     # Обработка каждой команды
#     for command in commands:
#         if command in directions:
#             dx, dy = directions[command]
#             x += dx
#             y += dy
#     return x, y
#
#
# print(list(follow("fflff")))
# #
# # # These "asserts" are used for self-checking
# # assert list(follow("fflff")) == [-1, 4]
# # assert list(follow("ffrff")) == [1, 4]
# # assert list(follow("fblr")) == [0, 0]
# print("__________________________________________")
#
# from collections.abc import Iterable
#
#
# def replace_first(items: list) -> Iterable:
#     if not items:
#         return []
#     temp = items[0]
#     n = len(items)
#     for i in range(n - 1):
#         items[i] = items[i + 1]
#     items[n - 1] = temp
#     return items
#
#
# # These "asserts" are used for self-checking
# print("Example:")
# print(list(replace_first([1, 2, 3, 4])))
#
# assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# assert replace_first([1]) == [1]
# assert replace_first([]) == []
# print("__________________________________________")
#
# from typing import List, Any
#
#
# def all_the_same(elements: List[Any]) -> bool:
#     elements = set(elements)
#     if not elements or len(elements) == 1:
#         return True
#     else:
#         return False
#
#
# print("Example:")
# print(all_the_same([]))
#
# # These "asserts" are used for self-checking
# assert all_the_same([1, 1, 1]) == True
# assert all_the_same([1, 2, 1]) == False
# assert all_the_same([1, "a", 1]) == False
# assert all_the_same([1, 1, 1, 2]) == False
# assert all_the_same([]) == True
# assert all_the_same([1]) == True
#
# print("__________________________________________")
#
#
# def backward_string_by_word(text: str) -> str:
#     if not text:
#         return ""
#     l = text.split(" ")
#     print(l)
#     st = ""
#     for word in l:
#         st += word[::-1] + " "
#     return st.strip()
#
#
# print(backward_string_by_word("hello   world"))
#
# # These "asserts" are used for self-checking
# assert backward_string_by_word("") == ""
# assert backward_string_by_word("world") == "dlrow"
# assert backward_string_by_word("hello world") == "olleh dlrow"
# assert backward_string_by_word("hello   world") == "olleh   dlrow"
# assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"
# print("__________________________________________")
#
# """
# Ваша функція полягає в тому, щоб аналізувати коливання цін на акції
# з плином часу. Вона повинна визначити найбільш вигідну можливість,
# розрахувавши максимальний потенційний прибуток, який можна отримати
# в межах цих коливань. Це означає пошук найвищої ціни для продажу акцій після їх купівлі за найнижчою можливою ціною.
#
# Однак, якщо немає можливості отримати прибуток - наприклад, коли ціна
# акції постійно знижується або залишається незмінною - функція повинна
# повернути нуль, що вказує на відсутність реальної можливості
# для прибуткової транзакції.
# """
#
#
#
#
# def stock_profit(stock: list[int]) -> int:
#     if not stock:
#         return 0
#
#     min_price = float('inf')
#     max_profit = 0
#
#     for price in stock:
#         if price < min_price:
#             min_price = price
#         elif price - min_price > max_profit:
#             max_profit = price - min_price
#
#     return max_profit
#
#
#
# print(stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]))   #4
#
#
#
#
# print("__________________________________________")
#
# from collections.abc import Iterable
#
#
# def compress(items: list[int]) -> Iterable[int]:
#     if not items:
#         return []
#     res = [items[0]]
#     j=0
#     for i in range(len(items)):
#         print(i)
#         if items[i] != res[j]:
#             res.append(items[i])
#             j+=1
#     return res
#
#
# print(list(compress([1, 2, 3, 4])))
# print("__________________________________________")
#
# from collections.abc import Iterable
#
#
# def except_zero(items: list[int]) -> Iterable[int]:
#     new_items = sorted([x for x in items if x!=0])
#     print(new_items)
#     res = []
#     i=0
#     for num in items:
#         if num == 0:
#            res.append(num)
#         else:
#             res.append(new_items[i])
#             i+=1
#     return res
#
#
# print("Example:")
# print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# # These "asserts" are used for self-checking
# assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
# assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
# assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
# assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
# assert list(except_zero([0, 0])) == [0, 0]

print("__________________________________________")
#
# """
# маємо список [1, 2, 3, 4, 5] і нам потрібно видалити всі елементи,
# що йдуть після 3 - це 4 і 5.
# Тут можливі два граничні випадки:
# якщо межовий елемент не знаходиться, тоді список повертається
# у незмінному вигляді;
# якщо список порожній, він повертається порожнім.
# """
#
# from collections.abc import Iterable
#
#
# def remove_all_after(items: list[int], border: int) -> Iterable[int]:
#     new_items=[]
#     if not items:
#         return []
#     if border not in items:
#         return items
#     else:
#         i=0
#         while items[i]!=border:
#             new_items.append(items[i])
#             i+=1
#         new_items.append(border)
#         return new_items
#
#
# print(list(remove_all_after([1, 2, 3, 4, 5], 3)))
#
# # These "asserts" are used for self-checking
# assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
# assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
# assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
# assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
# assert list(remove_all_after([], 0)) == []
# assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
#
# print("__________________________________________")
"""
Твоя функция позволяет составить список списков, который представляет
двоякое решение из заданного количества рядов и колонок. 
Эта строка показывает сочетание чисел от начала до начала + строки * столбцы - 1 в ряду составления, 
но элементы каждого ряда с непарным индексом числа находятся 
в спадном ряду, тогда если читать числа в ростовом ряду, 
они идут зигзагом в счете.
"""
#
# def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
#     matrix = []
#     for i in range(rows):
#         row = [start + j for j in range(cols)]
#         if i % 2 != 0:
#             row.reverse()
#         matrix.append(row)
#         start += cols
#     return matrix


#
# print(create_zigzag(3, 5))

# # These "asserts" are used for self-checking
# assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
# assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
# assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]
# print("__________________________________________")




