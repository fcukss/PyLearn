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

from functools import reduce
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


def multiplier(n):
    def multiply_by(x):
        return x * n
    return multiply_by

times_three = multiplier(3)    #n=3
result = times_three(10)   #x=10  10*3
print(result)   #30