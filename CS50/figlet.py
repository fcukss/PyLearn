import sys
import random
import pyfiglet

def get_figlet():
    # Получаем список аргументов командной строки (без имени скрипта)
    args = sys.argv[1:]

    # Получаем список доступных шрифтов
    available_fonts = pyfiglet.Figlet().getFonts()

    # Проверяем аргументы
    if len(args) == 0:
        font = random.choice(available_fonts)  # Выбираем случайный шрифт
    elif len(args) == 2 and args[0] in ("-f", "--font") and args[1] in available_fonts:
        font = args[1]  # Используем указанный пользователем шрифт
    else:
        sys.exit("Usage: python figlet.py [-f FONT_NAME]")

    # Запрашиваем у пользователя текст
    text = input("Введите текст: ")

    # Создаем объект Figlet с выбранным шрифтом
    figlet = pyfiglet.Figlet(font=font)

    # Выводим текст в формате ASCII-арта
    print(figlet.renderText(text))


get_figlet()