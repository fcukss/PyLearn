# def check_item_in_list(grocery_list, item):
#     for i, name in enumerate(grocery_list):
#         if item == name['name']:
#             print(item)
#             return
#         else:
#             print(f"Продукта {item} нет в списке")
#         break
#
#
# if __name__ == '__main__':
#     groceries = [{'name': 'Мясо', 'price': 100}, {'name': 'Рыба', 'price': 80}]
#     check_item_in_list(groceries, "Мясо")  # распечатает Мясо
#     check_item_in_list(groceries, "Молоко")


import time


# def count():
#     end_time = time.time() + 0.5
#     res = 0
#     while time.time() < end_time:
#         print(res)
#         time.sleep(0.1)
#         res += 1


#count()



# def time_to_wake_up(hours):
#     end_time = time.time() + 60 * hours
#     if (end_time - time.time()) > (60 * 8):
#         return True
#
#
# def check_sleep():
#     hours = 0
#     while True:
#         hours += time.time()
#         if time_to_wake_up(hours)==True:
#             break
#     return hours
#
#
# print(check_sleep())

# def log_function(f):
#     def wrap(*args, **kwargs):
#         print(f'Вызываем функцию {f}')
#         print(f'Входные параметры {args}')
#         print(f'Опциональные параметры {kwargs}')
#         result = f(*args, **kwargs)
#         print(f"Результат вызова функции {result}")
#         return result
#     return wrap
#
#
# @log_function
# def add_two_numbers(a, b):
#     return a + b
#
# add_two_numbers(5, 44)
#
# import  datetime
#
#
#
# def get_current_year():
#     now_date = datetime.datetime.now()
#     return now_date.year
#
# print('Текущий год:', get_current_year())
#

class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, first_name, last_name, passport_number):
        new_customer = Customer(first_name, last_name, passport_number)
        self.customers.append(new_customer)

    def get_customer(self, passport_number):
        for customer in self.customers:
            if passport_number == customer.passport_number:
                return customer
        raise KeyError()


bank = Bank()
bank.add_customer("John", "Dou", "CV453214")

customer = bank.get_customer("CV453214")


