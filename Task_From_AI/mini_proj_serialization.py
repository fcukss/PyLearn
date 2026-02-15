"""Задача:
Создай класс DNA_Sample с атрибутами id, sequence (строка типа "ACTG") и location (холодильник).
Создай список из трех таких объектов.
Сохрани этот список в файл samples.json (используй default=lambda x: x.__dict__ для простоты).
Напиши функцию, которая читает этот файл и с помощью DNA_Sample.from_dict создает новый список объектов.
Выведи sequence второго объекта из восстановленного списка."""
import json


class DNA_Sample:
    def __init__(self, id, sequence, location = 'Fridge'):
        self.id = id
        self.sequence = sequence
        self.location = location

    def __len__(self):
        return len(self.sequence)

    def __gt__(self, other):
        return self.__len__() > len(other)

    def __add__(self,other):
        return DNA_Sample(id = self.id + other.id,
                          sequence=self.sequence + other.sequence)

    def __getitem__(self, index):
        return self.sequence[index]

    def __iter__(self):
        return iter(self.sequence)

    def __contains__(self, sub_sequence):
        return sub_sequence in self.sequence


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

# restore_samples = read()
# obj = restore_samples[1]
# print(obj.sequence)   #CTGA

s1 = DNA_Sample(1, "ACTG")
s2 = DNA_Sample(2, "GGGG")
print(len(s1))        # Должно вывести 4
print(s1 > s2)        # Должно вывести False
s3 = s1 + s2
print(s3.id)
print(s3.sequence)
print('---------------')
sample = DNA_Sample(1, "ACTG")

print(sample[0])            # Должно вывести 'A'
print("CT" in sample)       # Должно вывести True

for nucl in sample:         # Должно по очереди напечатать A, C, T, G
    print(nucl)