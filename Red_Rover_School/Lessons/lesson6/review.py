# add = lambda x, y: x + y
# print(add(5, 8))  # 13
#
# numbers = [1, 2, 3, 5, 6, 7, 10]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # [1, 4, 9, 25, 36, 49, 100]
#
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # [2, 6, 10]
#
# #sorted for student's age
# students = [('John',22), ('Anna', 19), ('Tom', 25)]
# sorted_students = sorted(students, key=lambda student: student[1])
# print(sorted_students)    #[('Anna', 19), ('John', 22), ('Tom', 25)]

#from functools import reduce
#
# #возращает одно значение
# numbers = [1, 2, 3, 5, 6, 7, 10]
# sum_numbers = reduce(lambda x,y: x + y, numbers)
# print(sum_numbers)    #34
#
#
# max_value = reduce(lambda x,y: x if x>y else y, numbers)
# print(max_value)  #10
#
# from itertools import accumulate
#
# lst = [1, 3, 4, 10, 4]
#
# print(list(accumulate(lst, lambda x, y: x + y)))  # [1, 4, 8, 18, 22]
# print(reduce(lambda x, y: x + y, lst))             #22



#print("==================================================================")

#
# def multiplier(n):
#     def multiply_by(x):
#         return x * n
#     return multiply_by
#
# times_three = multiplier(3)    #n=3
# result = times_three(10)   #x=10  10*3
# print(result)   #30


#print("==================================================================")


# def calculator():
#     def add(a,b):
#         return a+b
#
#     def subtract(a,b):
#         return a-b
#
#     return add, subtract
#
# add_func, subtract_func=calculator()
# print(add_func(5,7))              #12
# print(subtract_func(10,6))        #4

#print("==================================================================")

# def log_decorator(func):
#     def wrapper(*args,**kwargs):
#         print(f"Function {func.__name__}() called with arguments {args},{kwargs}")
#         result = func(*args,**kwargs)
#         print(f"Function {func.__name__}() returned: {result}")
#         return result
#     return wrapper
#
# @log_decorator
# def add(a,b):
#     return a+b
#
# add(5,10)


#print("==================================================================")


# import time
# def timer_decorator(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         result = func(*args,**kwargs)
#         end_time = time.time()
#         print(f"Function {func.__name__}() took {end_time-start_time: .4f} seconds to run")
#         return result
#     return wrapper
#
# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("func finished")
#
# slow_function()

#print("==================================================================")

#
# def requires_permission(user_role):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if user_role!= 'admin':
#                 print("Access Denied: You don't have permission to this function.")
#                 return
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
# @requires_permission(user_role = 'user')
# def delete_database():
#     print("Database deleted")
#
# delete_database()


print("======================Counter===================================")

from collections import Counter


fruits = ['apple', 'banana', 'orange','kiwi','apple']
fruit_count = Counter(fruits)
print(fruit_count)     #Counter({'apple': 2, 'banana': 1, 'orange': 1, 'kiwi': 1})

word = "programming"
char_count = Counter(word)
print(char_count)     #Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})


counter = Counter({'a':3, 'b':1})
print(list(counter.elements()))     #['a', 'a', 'a', 'b']

counter.subtract({'a':1, 'b':2})
print(counter)                      #Counter({'a': 2, 'b': -1})

