import json
import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

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
doctors_path = os.path.join(current_dir, 'data', 'doctors.json')
items_path = os.path.join(current_dir, 'data', 'items.json')
prescriptions_path = os.path.join(current_dir, 'data', 'prescriptions.json')


db_doctors = JSONDatabase(doctors_path)
db_items = JSONDatabase(items_path)
db_prescriptions = JSONDatabase(prescriptions_path)