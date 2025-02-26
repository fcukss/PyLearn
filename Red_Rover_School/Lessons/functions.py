# создаем функцию с множеством аргументов
def func(*args):
    print(args)  # (1, 2, 3, 4, 54, 5, 6, 67, 4, 7, 8, 7, 54)


func(1, 2, 3, 4, 54, 5, 6, 67, 4, 7, 8, 7, 54)

numbers = [1, 32, 54, 56, 32, 6, 67, 6, 75, 34, 43, 5]
print(sum(numbers))


def my_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(my_sum(numbers))

print("+++++++++++++++++++++++++++++++++++++++++")

# изменяем переменную из гловбальной области
a = 10


def func():
    global a
    a += 2


func()
print(a)  # 12

print("+++++++++++++++++++++++++++++++++++++++++")

x = 1
y = 1


def left():
    global x
    x += 1


def up():
    global y
    y += 1


def draw_player():
    print(f"x = {x},y = {y}")


left()
left()
left()
up()
up()

draw_player()  # x = 4,y = 3

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

n = 5
n = 'Hello'


def add(a: int, b: int) -> int:
    """

    :param a:
    :param b:
    :return:
    """
    return a + b


# написание типов в аргументов не имеет никакого значения. это для читаемости
print(add('Hello', 'World'))  # HelloWorld
