"""Создай словарь mri_status, который содержит:
device_id: "MRI-NX-2000"
helium_level: 92 (в процентах)
temperatures: список из трех чисел [15.5, 16.2, 15.8] (градусы Цельсия)
is_active: True
Используй модуль json, чтобы превратить этот словарь в строку и записать в файл status.json.
Важно: сделай JSON "красивым" (с отступами в 4 пробела), чтобы инженер мог прочитать его глазами."""
import json
#
# mri_status = {
#     'device_id': 'MRI-NX-2000',
#     'helium_level': 0.92,
#     'temperatures': [15.5, 16.2,15.8],
#     'is_active': True,
# }
#
# def create_json(dct):
#     return json.dumps(dct, indent=4)
#
# def write_to_file(value):
#     with open('status.json', 'w') as file:
#         file.write(value)
#
# #Version from AI пишет сразу в поток, меньше использует память
# def write_to_file_AI(dct):
#     with open('status2.json', 'w') as file:
#         json.dump(dct, file, indent=4) # dump (без s) пишет сразу в поток
#
#
#
# write_to_file(create_json(mri_status))
# write_to_file_AI(mri_status)
#

"""
Часть 2: Десериализация (Чтение)
Напиши код, который открывает файл status.json и превращает его обратно в Python-словарь.

Добавь проверку: если helium_level меньше 95%, выведи в консоль сообщение: 
"ALARM: Low Helium Level!".
"""

# def open_json():
#     with open('status.json') as json_data:
#         res = json.load(json_data)
#         if res['helium_level']*100 < 95:
#             print("ALARM: Low Helium Level!")
#
# open_json()


"""final Task
Создай объект customer = Customer("Tom", "Riddle", "FL342312").
Попробуй распечатать customer.__dict__.
Попробуй сохранить этот customer.__dict__ в JSON файл.
"""

class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_dict(cls, data):
        # cls — это сам класс Customer
        # **data распаковывает ключи словаря в аргументы конструктора
        return cls(**data)


if __name__ == '__main__':

    customer = Customer("Tom", "Riddle", "FL342312")
    print(customer.__dict__)
    with open('customer.json', 'w') as file:
        json.dump(customer.__dict__, file)

"""В json.dump есть секретный аргумент default. 
Это функция, которая говорит JSON-у: 
"Если встретишь то, что не знаешь как сохранить — используй эту логику"."""

def my_serializer(obj):
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    raise  TypeError(f"Object of type {type(obj)} is not JSON serializable")

customers = [
    Customer("Tom", "Riddle", "FL342312"),
    Customer("Harry", "Potter", "HP999000")
]

with open('all_customers.json', 'w') as file:
    # JSON сам вызовет my_serializer для каждого Customer
    json.dump(customers,file, default=my_serializer, indent=2)


# --- ТЕСТ: Жизненный цикл данных ---
original_customer = Customer("Tom", "Riddle", "FL342312")

# В JSON (Сериализация)
json_str = json.dumps(original_customer.__dict__)

# Из JSON обратно (Десериализация)
loaded_json = json.loads(json_str) # Сейчас это просто словарь {}

#Оживляем объект!
new_customer = Customer.from_dict(loaded_json)

print(new_customer.get_full_name())  #Tom Riddle
