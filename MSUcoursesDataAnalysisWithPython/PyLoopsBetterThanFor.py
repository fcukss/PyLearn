from time import perf_counter
import random

"""
используем вместо классического фикла for встроенную функцию sum()
счетчик показівает скорость віполнения больше почти в 2х
"""


def cycle_exmpl():
    res = 0
    N = [num for num in range(1_000_000)]

    for num in N:
        res += num
    print(res)


def sum_example():
    N = [num for num in range(1_000_000)]
    print(sum(N))


# if __name__=="__main__":
#     start = perf_counter()
#     cycle_exmpl()
#     print(f"time:{(perf_counter()-start):.02f}")
#
#     start = perf_counter()
#     sum_example()
#     print(f"time:{(perf_counter() - start):.02f}")


"""
доступ по индексам
"""


def index_access():
    temp = 0
    numbers = [num for num in range(1_000_00_00)]

    for num in range(len(numbers)):
        temp = numbers[num]
    print(temp)


def enumerate_exapmle():
    temp = 0
    numbers = [num for num in range(1_000_00_00)]
    # можно получить два значения за один проход
    for index, num in enumerate(numbers):
        temp = num
    print(temp)


# if __name__=="__main__":
#     start = perf_counter()
#     index_access()
#     print(f"time:{(perf_counter()-start):.02f}")
#
#     start = perf_counter()
#     enumerate_exapmle()
#     print(f"time:{(perf_counter() - start):.02f}")

"""
перебор по двум спискам
"""


def stupid_expl():
    # можно выйти за пределы списка
    res = 0
    a = [num for num in range(1_000_000)]
    b = [num for num in range(1_000_000)]

    for i in range(len(a)):
        res = a[i] + b[i]
    print(res)


def zip_example():
    res = 0
    a = [num for num in range(1_000_000)]
    b = [num for num in range(1_000_000)]
    for a_val, b_val in zip(a, b):
        res = a_val + b_val
    print(res)


# if __name__ == "__main__":
#     start = perf_counter()
#     stupid_expl()
#     print(f"time:{(perf_counter() - start):.02f}")
#
#     start = perf_counter()
#     zip_example()
#     print(f"time:{(perf_counter() - start):.02f}")


"""
использование глобальной переменной
нужно подсчитать кол-во подтвержлденных покупок
"""

USERs_BUY = [
    ("confirmed", 100),
    ("unconfirmed", 500),
    ("confirmed", 900)
]


def fill_users_list():
    global USERs_BUY
    temp = [("confirmed", random.randint(10, 200)) for user in range(1_000_000)]
    USERs_BUY += temp

# with using loop
def cycle_example():
    res = 0

    for user in USERs_BUY:
        if user[0] == "confirmed":
            res += user[1]
    print(res)


#with using list comprehansion
def list_exaple():
    balance_list = [user[1] for user in USERs_BUY if user[0]=="confirmed"]
    res = sum(balance_list)
    print(res)

#with generator
def generator_exaple():
    balance_list = (user[1] for user in USERs_BUY if user[0] == "confirmed")
    res = sum(balance_list)
    print(res)

if __name__ == "__main__":
    fill_users_list()
    start = perf_counter()
    cycle_example()
    print(f"time:{(perf_counter() - start):.02f}")

    start = perf_counter()
    list_exaple()
    print(f"time:{(perf_counter() - start):.02f}")

    start = perf_counter()
    generator_exaple()
    print(f"time:{(perf_counter() - start):.02f}")