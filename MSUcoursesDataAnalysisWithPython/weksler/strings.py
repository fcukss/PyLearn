# name = "Egor"
# last_name = "Wexler"
# print(name + last_name)
#
# name = "Luke"
# last_name = "SkyWalker"
# print("Hello, my name is {} {}".format(name, last_name))
# print(f"Hello, my name is {name} {last_name}")


# def get_list_of_groceries(text=str):
#     list_of_groceries = text.split()
#     print(list_of_groceries)
#     for grocery in list_of_groceries:
#         print(grocery)
#
#
# text = 'Молоко, Яйца, Сахар, Соль'
# list_of_groceries = text.split()
# print(list_of_groceries)
# get_list_of_groceries(text)
#
# phrase = '  hello, my name is Egor'
# phrase_list = phrase.split()
# print(phrase_list)


# a ="001001"
# print(a.lstrip('0'))   #1001
# b = "00100100"
# print(b.rstrip('0'))   #001001


print("xxcxc " * 5)   #xxcxc xxcxc xxcxc xxcxc xxcxc
print(" " * 5)  #      - 5 пробелов

#проверка слова на палиндром
def is_palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False


from time import perf_counter

#my variant
def parse_poem(text):
    poem_dict = {}
    poem_list = text.split()
    poem_temp =[]
    for word in poem_list:
        word = str(word).strip('", !')
        if not str.islower(word) and len(word)>1:
            poem_temp.append(word)
    for i in range(len(poem_temp)):
         if i%2!=0:
             poem_dict[poem_temp[i-1]] = poem_temp[i]
    return poem_dict

#wexler's variant
def parse_poem_wex(poem):
    res = {}
    animal = None
    #делим стихотворение на строчки
    for line in poem.split('\n'):
        #убираем пустые строки
        if not line:
            continue
        #если мы не видили животных
        if animal is None:
        #определим живтоное как первое слово в строчке
            animal = line.split(' ')[0]
        #при усдовии что строчка начинается с тире
        elif line.startswith('-'):
        #уберем тире и другие символы и оставляем одно слово
            line = line.replace('-','').replace('!','').split(',')[0].strip()
        #заполнили dictionary значениями
            res[animal] = line
        #опустошаем перевенную и готовимся к следующему
            animal =None


    return res

if __name__ == '__main__':
    start = perf_counter()
    poem = """
Свинки замяукали:
- Мяу, мяу!
Кошечки захрюкали:
- Хрю, хрю, хрю!
Уточки заквакали:
- Ква, ква, ква!
Курочки закрякали:
- Кря, кря, кря!
Воробышек прискакал
И коровой замычал:
- Мууу!
"""

    poem2 = """Кукушка на суку:
"Не хочу кричать куку,
Я собакою залаю:
- Гав, гав, гав!"""

#parse_poem(poem)
print(parse_poem(poem))
print(f"time:{(perf_counter() - start)}")