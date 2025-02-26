
def check_age():
    print("enter your age")
    age  = int(input())
    if age >18 and age<21:
        print("Buy rom")
    elif age < 18:
        print("Buy cola")
    else:
        print("Buy bear")

check_age()

"""
Анекдот
Жена отправляет мужа-программиста в магазин:
— Купи батон хлеба, если будут яйца — возьми десяток.
Муж возвращается из магазина с десятью батонами.
— Ты зачем столько хлеба купил?
— Так ведь яйца были...
Напишите функцию go_shopping, которая реализует этот анекдот. Она должна распечатать (print), что купил муж в зависимости от ситуации. (То есть, "Купил десять батонов", "Купил батон")
Есть ли яйца в наличии - определяет входной параметр
"""

def go_shopping(eggs):
    if eggs:
        print("Купил десять батонов")
    else:
        print("Купил батон")


go_shopping(True)
go_shopping(False)
go_shopping(100)
go_shopping(0)





def evaluate (num1, num2):
    if num1 and num2 == 0:
        print('both numbers are zero')
    elif num1 or num2 == 0:
        print('one of the numbers is zero')
    else:
        print('both numbers are not zero')

evaluate(0,0)