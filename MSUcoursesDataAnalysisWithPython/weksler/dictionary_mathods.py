
person = {
    "name": "Han",
    "last name": "Solo"
}


print(person['name'])   #Han

print(person.items())   #dict_items([('name', 'Han'), ('last name', 'Solo')])
print(person.keys())  #dict_keys(['name', 'last name'])
print(person.values())  #dict_values(['Han', 'Solo'])

#будет ошибка и программа завалится
#print(person['taet'])

#что б этого избежать можно зделать так
print(person.get('test'))  #None - значение по умолчанию
#или сами вводим значение по умолчанию
print(person.get('test', "Такого ключа нет"))

#удаляет последний элемент из дикшинари и возвращает его
print(person.pop('name'))  #Han
#если удаляеш элемент по неправильному ключу то будет ошбка
# или пишеш значение по умолчанию
print(person.pop('test', "нет такого")) #нет такого

#add element to dictionary
person ['age'] = 33
print(person) # {'last name': 'Solo', 'age': 33}
