grocery_list = ['bread', 'milk', 'cheese']
#
len(grocery_list)
#
# for i in grocery_list:
#     print(f"продукт  {i}")
#

print(list(range(10)))   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(5,10,3):
    print(f"Hello{i}")

for i in enumerate(grocery_list):
    print(i[0])

#распаковываем лист
a, b ,c = [1, 2, 3]
print(a, b,c)       #1 2 3
print(b)             # 2

grocery_list  = [{'name':'avocado'}, {'name': 'milk'}]

for index, name in enumerate(grocery_list):
    print(index, name['name'])


def even_numbers(target):
    for number in range(target):
        if number % 2 == 0:
            print(number)


def odd_numbers(target):
    for number in range(target):
        if number % 2 != 0:
            print(number)



print("+++++++++++++++++++++++++++++++++++++")
import datetime

today = datetime.date.today()

print("+++++++++++++++++++++++++++++++++++++")
import time

def count():
    i = 0
    end_time = time.time() + 0.5
    while time.time() < end_time:
        time.sleep(0.1)
        print(i)
        i += 1


count()