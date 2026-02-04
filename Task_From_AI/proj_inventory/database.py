import json
import os.path

class JSONDatabase:
    def __init__(self, filename:str):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                res = json.load(file)
            return res
        except (json.JSONDecodeError, ValueError):
            print(f'Error: file {self.filename} is corrupted')
            return []

    def save(self, data):
        """Полностью перезаписывает файл новым списком."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def delete(self, item_id):
        data = self.load()
        # Создаем новый список, исключая элемент с нужным ID
        new_data = [item for item in data if item['id'] != item_id]
        if len(new_data) == len(data):
            return False  # Ничего не нашли для удаления
        self.save(new_data)
        return True

db_items = JSONDatabase("data/hospital.json")
db_doctors = JSONDatabase('data/doctors.json')
db_prescriptions = JSONDatabase("data/prescriptions.json")