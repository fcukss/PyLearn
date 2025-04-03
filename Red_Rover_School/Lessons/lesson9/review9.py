# import os
# import time
#
# with open('names.txt', 'w') as f:
#     f.write('Mark Berg\nLian Mellon\nAdel Mongomarry\nIlon Mask')
#
# file_path = "names.txt"
#
# # get metadata using os.stat()
# file_metadata = os.stat(file_path)
#
# # extract specefic metadata
# file_size = file_metadata.st_size
# print(f"File size: {file_size} bytes")  # file size in bytes
#
# last_modified = file_metadata.st_mtime
# print(f"Last modified: {time.ctime(last_modified)}")  # last modification time
#
# creation_time = file_metadata.st_ctime
# print(f"Create :{time.ctime(creation_time)}")
#
# last_accessed = file_metadata.st_atime  # last access time
# print(f"Last access {time.ctime(last_accessed)}")

# =======Excwptions=====

# res = "2" + 2  # TypeError
#
# lst = [1,2,3]
# print(lst[4])  #IndexError
#
# number = int("ABC") # ValueError
#
# dictionary = {'name':"bob"}
# print(dictionary['age']) # KeyError
#
# file = open("asfafaf.af")  #FileNotFoundError
#

# try:
#     num1 = int(input("Enter a num: "))
#     num2 = int(input("Enter another num: "))
#     res = num1/num2
# except ValueError:
#     print("invalid number")
# except ZeroDivisionError:
#     print("you divide by zero")
#

# try:
#     num = int(input("Enter a num: "))
# except ValueError:
#     print("Invalid num")
# else:
#     print(f"Your num is {num}")

# ================JSON================

import json


##deserialization - преобразование из json
# json_data = '{"name": "Alice", "age": 24, "is_student": true}'
# python_dict = json.loads(json_data)
# print(python_dict)   #{'name': 'Alice', 'age': 24, 'is_student': True}

# #serialization - преобразование в json
# python_dict = {'name': 'Alice', 'age': 24, 'is_student': True}
# json_data = json.dumps(python_dict)
# print(json_data)  #{"name": "Alice", "age": 24, "is_student": true}

# #Reading
# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(data)

# #writing
# python_dict = {'name': 'Alice', 'age': 24, 'is_student': True}
# with open('output.json', 'w') as file:
#     json.dump(python_dict,file)

# #если json не правильный
# json_data =  '{"name": "Alice", "age": 24'
# try:
#     python_data = json.loads(json_data)
# except json.JSONDecodeError as e:
#     print(f"Error: {e}")


