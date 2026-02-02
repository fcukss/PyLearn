#Конвертировать dict в string (->JSON)
import json      # не забывайте импортировать модуль

film = {'name': 'A new Hope', 'available': None}

film_str = json.dumps(film)     # конвертирует dict в string

print(film_str)    #{"name": "A new Hope", "available": null}

# dict -> str -> save to .json

import json

film = {'name': 'A new Hope', 'available': None}    # dict

with open('my_film.json', 'w') as file:
    value = json.dumps(film)  # перевели dict в str
    file.write(value)            # записали в файл под названием my_film.json

"""Однако, чтобы сохранить json-файл на жёсткий диск - 
можно воспользоваться и более коротким вариантом, доступным в модуле json:"""
import json

film = {'name': 'A new Hope', 'available': None}

with open("my_film.json", 'w') as file:
    json.dump(film, file)


"""В обратную сторону: конвертировать JSON в dict"""
import json

film = '{"name": "A new Hope", "available": null}'   # str

film_dict = json.loads(film)

print(film_dict)   #{'name': 'A new Hope', 'available': None}

# Прочитать из файла
with open('my_film.json', 'r') as f:
    film = json.load(f)

# Метод loads принимает str, а возвращает dict
# Метод load принимает открытый файл, а возвращает dict