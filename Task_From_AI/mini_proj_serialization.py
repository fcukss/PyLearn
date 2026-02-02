"""Задача:
Создай класс DNA_Sample с атрибутами id, sequence (строка типа "ACTG") и location (холодильник).
Создай список из трех таких объектов.
Сохрани этот список в файл samples.json (используй default=lambda x: x.__dict__ для простоты).
Напиши функцию, которая читает этот файл и с помощью DNA_Sample.from_dict создает новый список объектов.
Выведи sequence второго объекта из восстановленного списка."""
import json


class DNA_Sample:
    def __init__(self, id, sequence, location):
        self.id = id
        self.sequence = sequence
        self.location = location

    @classmethod
    def from_dict(cls, dct):
        return cls(**dct)


list_dna = [DNA_Sample(111,'ACTG', 'fridge'),
            DNA_Sample(115, 'CTGA', 'fridge'),
            DNA_Sample(117, 'ATCG', 'fridge')]

with open('samples.json', 'w') as file:
    json.dump(list_dna,file, default=lambda x: x.__dict__, indent= 2)

def read():
    with open('samples.json', 'r') as data:
        loaded_samples = json.load(data)
        return [DNA_Sample.from_dict(item) for item in loaded_samples]

restore_samples = read()
obj = restore_samples[1]
print(obj.sequence)   #CTGA