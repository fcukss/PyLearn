"""Задача:

Возьми свой класс DNA_Sample.
Модифицируй метод from_dict так, чтобы он проверял наличие всех ключей в словаре.
Если какого-то ключа (например, location) нет в JSON,
метод должен выбрасывать ошибку KeyError с текстом "Missing data in JSON: location".

Напиши основной блок кода, который:
Пробует прочитать файл samples.json.
Если файла нет — создает его с одним стандартным образцом (Default Sample).
Если файл есть, но данные в нем битые (не хватает ключей) — выводит ошибку и не падает."""

import json

class DNA_Sample:
    def __init__(self, id, sequence, location):
        self.id = id
        self.sequence = sequence
        self.location = location

    @classmethod
    def from_dict(cls, dct):
        # Проверяем наличие всех необходимых ключей перед созданием объекта
        required_fields = ['id', 'sequence', 'location']
        for field in required_fields:
            if field not in dct:
                raise KeyError(f"Missing data in JSON: {field}")
        return cls(**dct)

# list_dna = [DNA_Sample(111,'ACTG', 'fridge'),
#             DNA_Sample(115, 'CTGA', 'fridge'),
#             DNA_Sample(117, 'ATCG', 'fridge')]

def load_samples():
    filename = "samples.json"
    try:
        with open(filename,'r') as file:
            data = json.load(file)
            return [DNA_Sample.from_dict(item) for item in data]
    except FileNotFoundError:
        print(f'filename{filename} not found. Create defaulrt sample')
        default_sample = [DNA_Sample(000, None, 'default')]
        with open(filename, 'w') as f:
            json.dump(default_sample,f, default=lambda x:x.__dict__, indent=2)
            return default_sample

    except (json.JSONDecodeError, KeyError) as e:
        print(f"ERROR {e}: 'samples.json' is corrupted (invalid format).")
        return []

samples = load_samples()
print("Final samples list:", samples)