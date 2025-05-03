# ================ITERATOR=========================================

# lst = ["first","second", "third",'four']
# it = iter(lst)   #преобразовали лист в итератор
# print(next(it))   #first
# print(next(it))   #second
# print(next(it))   #third
# print(next(it))   #four
# print(next(it))   #erorr stop iteration

# """
# лист  - это итерируемый обьект но не итератор
# """
# my_lst = [1, 2, 3]
# a = 10
# print(hasattr(my_lst, '__iter__'))  # True  It is an iterable not Iterator!
# print(hasattr(my_lst, '__next__'))  # False it is not Iterator
# # print(next(my_lst))               # TypeError 'list' object is not an iterator
# print(hasattr(a, '__iter__'))       # False   this is not iterable
#
# my_iterator = iter(my_lst)
# print(hasattr(my_iterator, '__iter__'))  # True
# print(hasattr(my_iterator, '__next__'))  # True
# print(next(my_iterator))  # 1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # implementation ItERATOR
# class CountUp:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1
#
#
# count_up = CountUp(1, 5)
# for num in count_up:
#     print(num)
#+++++++++++++++++++++++++++++++++++++++++++++++++