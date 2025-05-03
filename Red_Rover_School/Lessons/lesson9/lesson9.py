# #create exception
# class FirstNameError(Exception):
#     pass
#
#
#
# def greet(name):
#     if not isinstance(name, str):
#         raise TypeError("no correct type")
#
#     if not name.isalpha():
#         raise FirstNameError(f"{name}  - not the name")
#
#     print(f"hi, {name}")
#
# greet("123")
#

#=====================FILE I/O=======================
with open("data.txt", 'a', encoding="utf-8") as file:
    file.write("Привет\n")

with open("data.txt", 'r', encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
#
#
# ==============JSON==================
# import json
#
# #serelisation - запись в файл
# with open("info.json", 'w') as file:
#     json.dump({'hello': 123}, file)
#
# #deserealisation - чтение из файла
# with open("info.json", 'r') as file:
#     data = json.load(file)
#
# print(data)
