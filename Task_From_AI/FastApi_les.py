"""
Задача: "Star Wars Filter & Stat"
Твои цели:

Написать функцию get_filtered_people(eye_color: str),
которая запрашивает список людей с первой страницы API (https://swapi.tech/api/people/).

Для каждого персонажа из списка нужно сходить по его персональной ссылке
(как мы делали в get_person) и проверить его eye_color.

Вернуть объект Pydantic, который содержит:

Список имен подходящих персонажей.
Их средний рост.
"""

from pydantic import BaseModel
from typing import List
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CharacterStats(BaseModel):
    matching_names: List[str]
    average_height: float
    total_found: int

def get_filtered_people(target_color: str) -> CharacterStats:
    global height_raw
    current_url = "https://swapi.tech/api/people/"
    lst = []
    total_height = 0.0

    # Цикл будет идти, пока в ответе есть ссылка на следующую страницу
    while current_url:
        print(f"Сканирую страницу: {current_url}")
        response = requests.get(current_url, verify=False).json()

        for item in response['result']:
            p_data = requests.get(item['url'], verify=False).json()
            props = p_data['result']['properties']

            if props['eye_color'].lower() == target_color.lower():
                lst.append(props['name'])

            height_raw = props.get('height')
            if height_raw and height_raw.isdigit():
                total_height += float(height_raw)
        # Переходим к следующей странице (API само даст ссылку или None)
        current_url = response.get('next')
    # Считаем среднее безопасно
    count = len(lst)
    avg_height = total_height / count if count > 0 else 0.0

    return CharacterStats(matching_names=lst,
                          average_height=avg_height,
                          total_found=len(lst))

get_filtered_people('blue')
