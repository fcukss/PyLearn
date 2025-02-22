"""
Ця функція повинна приймати на вхід основний рядок
та підрядок і повертати кількість входжень підрядка
в основному рядку. Вона не повинна бути чутливою
до регістру і може перекриватися.
"""

import re

def count_occurrences(main_str: str, sub_str: str) -> int:
    # count = main_str.lower().count(sub_str)
    overlapping_count = len(re.findall(f'(?={sub_str.lower()})', main_str.lower()))
    return overlapping_count



print(count_occurrences("appleappleapple", "appleapple"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1
