# from Red_Rover_School.Lessons import functions
# import math
#
# print(functions.add(5, 10))
#
# print(functions.pi)    #3.14
# print(math.pi)         #3.141592653589793
#
# #
# numbers =  [12, "fdsg", functions.add(5,9)]
# print(numbers)    #[12, 'fdsg', 14]
#
# func = print
# func("Hello world")       #Hello world

def my_map(func, items):
    res = []
    for i in items:
        res.append(func(i))
    return res


def pow(x):
    return x ** 2


numbers = [1, 2, 3]
# передаем функцию в аргумент без скобок
print(my_map(pow, numbers))    #[1, 4, 9]
