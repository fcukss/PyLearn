"""
посчитаем обьем комнаты
"""


# simple
def simple_var(numbers: str) -> int:
    sizes = numbers.split(",")
    x = sizes[0]
    y = sizes[1]
    z = sizes[2]
    return int(x) * int(y) * int(z)


print(simple_var("10,50,80"))


def unpackage_var(numbers: str) -> int:
    x, y, z, = map(int, numbers.split(","))
    return x * y * z


print(unpackage_var("10,50,80"))

from functools import reduce


def reduce_var(numbers: str) -> int:
    res = reduce(
        lambda a, b: a * b,
        map(int, numbers.split(","))
    )
    return res


print(reduce_var("10,50,80"))

numbers = [10, 50, 20, 20]
sum = reduce(lambda a, b: a + b, numbers)
print(sum)  #100
