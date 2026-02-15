"""реализуем шифр виженера
Цикличность ключа:
Текст обычно длиннее ключа, поэтому ключ нужно повторять.
Например, если текст PYTHON (6 букв), а ключ ABC (3 буквы),
то для шифрования мы используем ABCABC.

Математическая формула:
Если представить буквы как числа (A=0, B=1, ..., Z=25),
то формула зашифрованного символа выглядит так:
 Ci = (Pi + Ki) \mod 26

 Где:Ci — зашифрованная буква.
 Pi — буква открытого текста.
 Ki — буква ключа.
 \mod 26 — остаток от деления на количество букв в алфавите (чтобы не выйти за его пределы).

"""
from itertools import cycle

def vigenere_encrypt(text, key, decrypt = False):
    result = []
    # Создаем бесконечный цикл из кодов букв ключа
    # Пример: для "ABC" это будет 0, 1, 2, 0, 1, 2...
    key_code = [ord(k.upper()) - ord('A')for k in key if key.isalpha()]
    if not key_code:
        return "Error: Key must contain one literal"

    key_cycle = cycle(key_code)

    for char in text:
        if char.isalpha():
            # Определяем "базу" (A=65 или a=97)
            start = ord('A') if char.isupper() else ord('a')
            # Берем следующий сдвиг из ключа
            shift = next(key_cycle)
            if decrypt:
                shift = -shift
            new_char = chr((ord(char)-start+shift)%26 +start)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    print("Encrypt Vigenere(Latin)")

    while True:
        print("Chose the task:")
        print('Enter 1 if encrypt')
        print('Enter 2 if decrypt')
        print('3, Exit')
        choise = input()

        if choise =='3':
            print('Bye')
            break
        elif choise not in ['1','2']:
            print('incorrect value. Try once more')
            continue
        text = input("Enter text: ")
        key = input("Enter ket(word): ")

        is_decrypt = (choise== '2')
        result = vigenere_encrypt(text,key, decrypt=is_decrypt)
        label = 'Result'
        print(f"\n{'-' * 20}\n{label} {result}\n{'-' * 20}")

if __name__ == '__main__':
    main()





