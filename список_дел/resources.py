import json

import uvicorn

from test_json import entry


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def __str__(self):
        return self.title

    def json(self):
        res = {
            'title': self.title,
            #   'entries': [entry.title for entry in self.entries]    #list-comprehensions тоже самое что и цикл снизу
            # }
            # for entry in self.entries:
            #     res['entries'].append(entry.title)
            #   #получаем все вложенные подлисты
            'entries': [entry.json() for entry in self.entries]
        }
        return res

    @classmethod
    # cls - єто класс
    def entry_from_json(cls, value: dict):
        new_entry = cls(value['title'])
        # пробегаемся по дикшинари с помощью рекурсии углубляемся в список
        for item in value.get('entries', []):
            new_entry.add_entry(cls.entry_from_json(item))
        return new_entry


def print_with_indent(value, indent=0):
    indentation = "\t" * indent
    print(indentation + str(value))


new_entry = Entry.entry_from_json(entry)
new_entry.print_entries()
print(new_entry.json())

