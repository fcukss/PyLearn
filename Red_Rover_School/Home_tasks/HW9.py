"""TASK1

Регистрация (часть 1)

1. Напишите функцию registration(), которая принимает 2 аргумента -
username (строка) и password() (строка)
2. Функция должна проверить username, а именно:
    a. username является строкой.
    b. Длина этой строки минимум 4 символа и максимум 15.
    c. username состоит только из букв.
3. Если username некорректный, то функция должна вызвать исключение
ValueError.
4. Функция должна проверить password, а именно:
    a. password является строкой.
    b. Длина этой строки минимум 8 символов и максимум 45.
    c. password состоит только из букв и цифр.
5. Если password некорректный, то функция должна вызвать исключение
ValueError.
6. Если “регистрация” прошла успешно, то функция должна вернуть True.

Дополнительно: создайте свой тип исключения RegistrationError и используйте
его вместо ValueError.
"""

class RegistrationError(Exception):
    pass

def registration(username: str, password : str):
    if not isinstance((username and password),str) :
        raise RegistrationError
    if not 4<=len(username)<=15 or not 8<=len(password)<=45:
        raise RegistrationError
    if not username.isalpha() or not password.isalnum():
        raise RegistrationError
    return True



# def main():
#     try:
#         registration("stas", "qwer52345435ty")
#     except RegistrationError:
#         print("1")
#     try:
#         registration("stas", 3242343453453454)
#     except RegistrationError:
#         print("2")
#     try:
#         registration("stas", "sdfsdf9sd@_)fsdf9sdfsdfsd")
#     except RegistrationError:
#         print("3")
#     try:
#         registration("astasdfsdfsdf", "qwertyuo706k")
#     except RegistrationError:
#         print("4")
#
# main()


""" TASK 2
Регистрация (часть 2)

- Напишите программу, которая в бесконечном цикле запрашивает у
пользователя ввести логин и пароль и сохраняет их в соответствующие
переменные.
- Вызовите функцию registration из предыдущей задачи передав ей
введенные логин и пароль пользователя.
- Если в registration были переданы некорректные данные, то ваша
программа должна перехватить вызванное функцией исключение
RegistrationError и написать в консоль “Ошибка регистрации!”, а затем
снова попросить пользователя ввести данные.
- Если данные были введены корректно, то программа должна вывести
“Успешно!” и выйти из бесконечного цикла.
"""
def main():
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter pass: ")
            registration(username,password)
            print("Успешно!")
            break
        except RegistrationError:
            print("Ошибка регистрации!")
            continue


# if __name__ == '__main__':
#     main()




"""TASK3 Дорогой дневник...
- Создайте пустой текстовый файл journal.txt
- Программа должна в бесконечном цикле запрашивать пользователя
ввести строку, которая является одним из режимов: “прочитать”,
“записать”, “выйти”.
- Если пользователь ввел “записать”:
o Программа просит пользователя ввести еще одну стру,ок которая
будет записана в файл.
o Программа дозаписывает эту строку в файл journal.txt c новой
строки.

- Если пользователь ввел “прочитать”:
o Программа выводит на экран все содержимое файла journal.txt.
- Если пользователь ввел “выйти”:
o Программа пишет в консоль “Еще увидимся!”, выходит из
бесконечного цикла и завершается.
- Если пользователь ввел что-то другое:
o Программа ничего не делает, просто возвращается к следующей
итерации бесконечного цикла.
"""

def main_task2():
    while True:
        command = input("Enter command: ")
        match command:
            case "write":
                with open("journal.txt", 'a') as file:
                    text = input("Enter text: ")
                    file.write(f"{text}\n")
            case "read":
                with open("journal.txt",'r') as file:
                    for line in file:
                        print(line.rstrip())
            case "exit":
                print("Еще увидимся!")
                break


# if __name__ == '__main__':
#     main_task2()




"""
Повторение прошлого материала.

Ответьте на следующие вопросы:
1. Что такое класс и что такое экземпляр класса?
2. Какие типы данных вы знаете? Чем отличается список от кортежа?
"""

"""
Бонус (Эта задача необязательна 😁)

В папке с домашним заданием есть файл secret.json, который содержит словарь с
одним ключом pixels. Значение по этому ключу — это список, содержащий
вложенные списки. Попробуйте изучить эти данные и придумать, что с ними
можно сделать.
"""

import json

with open("secret.json", 'r') as file:
    data = json.load(file)

pixels = data["pixels"]
for row in pixels:
    text = ''
    for c, num in row:
        text+=c*num
    print(text)
