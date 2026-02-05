import pytest
from database import db_prescriptions, db_items

"""Автоматически очищает файл рецептов перед каждым тестом.
"""
@pytest.fixture(autouse=True)
def clean_prescription():
    #очищаем базу рецептов что б тест не проваливался
    db_prescriptions.save([])

    #восставнвливаем запас товаров
    items = db_items.load()
    for i in items:
        i['stock']=100
    db_items.save(items)
    yield