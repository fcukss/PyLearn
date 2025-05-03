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
#
# def my_map(func, items):
#     res = []
#     for i in items:
#         res.append(func(i))
#     return res
#
#
# def pow(x):
#     return x ** 2
#
#
# numbers = [1, 2, 3]
# # передаем функцию в аргумент без скобок
# print(my_map(pow, numbers))    #[1, 4, 9]
#
#
# print("==================map=====================")
#
# #встроенная функция map -> возврашает iterater
# result = map(pow,numbers)
# print(result)              #<map object at 0x0000016753A7B2B0>
# #для распечатки нужно упаковать в list или tuple
# print(list(result))        # [1, 4, 9]


# print("==================filter=====================")
#
# def function(x):
#     return x>10
#
# result = filter(function,[45,1,2,56] )
# print(list(result))          #[45, 56]


# print("==================lambda=====================")
#
# numbers = [42, 1, 2, 50, 56, 7, 8, 9, 20]
# #фильтруем список на числа меньше 10
# result = filter(lambda x: x < 10, numbers)
# print(list(result))  # [1, 2, 7, 8, 9]


# def mother(y):
#     x = 10
#
#     def son():
#         print(x,y)
#
#     return son
#
#
# #
# result = mother(4)
# # вызываетя функция son так как она в return mother()
# result()  # 10, 4


# string = "Global"
# def parent():
#     string = "no-local"
#
#     def child():
#         #string = "Local"
#         print(string)
#
#     return child
#
# func = parent()
# func()


# #именнованные параметры и на выходе получаем dict
# def functions(**kwargs):
#     print(kwargs)
# #неименнованые аргуенты и на выходе tuple
# def functions_2(*args):
#     print(args)
#
# functions(a=4, b=6, hello = True)    #{'a': 4, 'b': 6, 'hello': True}
# functions_2(4, 6,True)     #(4, 6, True)

# def functions_3(*args, **kwargs):
#     print(args,kwargs)
#
# functions_3(45,3,2, a = 25, b=36)  #(45, 3, 2) {'a': 25, 'b': 36}
# functions_3()  #() {}

# print("==================decorator=====================")

def logger(func):
    def wrapper(*args,**kwargs):
        print("start function with parameters", args, kwargs)
        result = func(*args,**kwargs)
        print("finisched functions with result: ", result)
        return result

    return wrapper

@logger
def greet():
    print("Hello!")
@logger
def add(a, b):
    return a+b


# dec_greet = logger(greet)
# dec_add= logger(add)
# dec_greet()
# dec_add(5,5)


greet()
print(add(2,5))