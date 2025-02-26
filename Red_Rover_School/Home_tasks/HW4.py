# """Task1
# """

# def creation_list():
#     return list([x for x in range(100) if x%2==0 and x%3==0])
#

# def creation_list_var_2():
#     list = []
#     for x in range(100):
#         if x%2==0 and x%3==0:
#             list.append(x)
#     return list


# print(creation_list())
# print(creation_list_var_2())
#
#
# """Task2
# """
#
# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
#
# def create_digi_list(arr)-> float:
#     numbers = []
#     for i in arr:
#         if isinstance(i,float) or isinstance(i,int):
#             numbers.append(i)
#     return sum(numbers)
#
# print(create_digi_list(items))

# """Task3
# """
#
# def create_message():
#         messages = []
#         while True:
#             string =  input("Enter a string: ")
#             if string == "Пока":
#                 print("Ну ладно, пока!")
#                 print(messages)
#                 break
#             messages.append(string)
#             if len(messages) > 5:
#                 messages.remove(messages[0])
#
# create_message()

#
# """Extension
# Task1
# """
#
# products = {
#      "apple": {"quantity": 10, "price": 100},
#     "banana": {"quantity": 20, "price": 50},
#     "orange": {"quantity": 15, "price": 80},
#     "grape": {"quantity": 8, "price": 120},
#     "milk":{"quantity": 12, "price": 90},
#      "bread": {"quantity": 30, "price": 40}
# }
#
#
# def increase_price(products):
#     for product, price in products.items():
#         price['price'] += price['price']*0.2
#     return products
#
# def remove_product(product):
#     products.pop(product)
#
# def sum_of_products(products):
#     sum = 0
#     for product in products.values():
#         sum += product['quantity'] * product['price']
#     return sum
#
# # print(increase_price(products))
# # remove_product('milk')
# # print(products)
# # products['salt'] = {"quantity": 7, "price": 12}
# # print(products)
# # print(sum_of_products(products))
#
# """Extension
# Task2
# """
# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
#
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]
# info={}
# for i in range(len(keys)):
#     info[keys[i]] = values[i]
# print(info)
#
#
# """Extension
# Task3
# """
#
# code = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
#
# cipher = {
#     "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
#     "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
#     "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
#     "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
#     "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
# }
#
# def decrypt(string):
#     res =''
#     for c in string:
#         if c  in cipher:
#             res += cipher[c]
#     return res
#
#
#
#
# def encrypt() :
#     text = input("enter the message: ")
#     res = ''
#     for c in text:
#         if c in cipher:
#            res+=res.join(cipher[c])
#     return res
#
# # print(decrypt(code))
# # print(encrypt())

"""Extension
Task4
"""

dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.
Doc: Вес тут совершенно ни при чем. """


dialog=dialog.lower()
letters ={}
for c in dialog:
    if c.isalpha():
        if c not in letters:
            letters[c] = 1
        else:
            letters[c]+=1
max = max(letters.values())
for letter, num in letters.items():
    if max==num:
        print(f"буква {letter}  - {max} раз")


#
# symbol = max(letters, key = letters.get)       #указывает, что для поиска максимума следует использовать значения словаря (т.е. количество вхождений букв), а не сами буквы как таковые.
# print(f"буква {symbol} - {letters[symbol]} раз")