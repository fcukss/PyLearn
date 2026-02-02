"""
Задача 1: "Валидатор из Татуина" (Уровень: Middle)
Цель: Научиться преобразовывать "грязные" данные
из внешнего API в строгие объекты Pydantic.
"""
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import requests
from fastapi import FastAPI, HTTPException

from typing import Optional     # импортируется в случае, если атрибут нужно сделать опциональным
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Starship(BaseModel):
    name: str
    model: str
    cost_in_credits: Optional[int] = None

    #проверяем значене поля cost_in_credits
    @field_validator('cost_in_credits', mode='before')
    @classmethod
    def get_cost(cls, value):
        if value =='unknown' or value is None:
            return None # Мы подменили "грязное" значение на валидное
        else:
            return value # Возвращаем как есть, если там что-то похожее на число

def get_ship():
    url = "https://swapi.tech/api/starships/9/"
    response = requests.get(url, verify= False)

    # Извлекаем только блок свойств
    properties = response.json()['result']["properties"]

    # Создаем объект модели. Pydantic сам сопоставит ключи!
    # Мы используем метод unpack (**), чтобы передать весь словарь
    return Starship(**properties)


ship = get_ship()

print(f"Ship is {ship.name} cost in cred = {ship.cost_in_credits}")



"""
Попробуй реализовать Агрегатор. 

У персонажа есть поле homeworld (ссылка). Напиши функцию, которая:

Получает персонажа.
Идет по ссылке из homeworld.
Возвращает объект Person, где в поле homeworld стоит не ссылка https://..., 
а название планеты, например "Tatooine".

Попробуешь сам собрать логику двух запросов в одной функции?"""




class Person(BaseModel):
    name: str
    homeworld: str


def get_person(person_id):
    person_url = f"https://swapi.tech/api/people/{person_id}/"
    p_res = requests.get(person_url, verify=False).json()
    p_data = p_res['result']['properties']

    home_url = p_data['homeworld']
    h_res = requests.get(home_url, verify=False).json()
    planet = h_res['result']['properties']['name']
    p_data['homeworld'] = planet
    return Person(**p_data)


person = get_person(1)
print(f"name : {person.name}, homeworld : {person.homeworld}")  #name : Luke Skywalker, homeworld : Tatooine

"""Задача №3
Напиши код, который сохраняет данные о планетах в обычный словарь (кэш).

Если мы уже загружали «Tatooine» для Люка, то для его сестры Леи 
мы не должны делать второй запрос к API планет, 
а должны просто взять название из нашего словаря.
"""

app = FastAPI()
# реальности этот кзщ меняем на Redis
PLANET_CACHE = {}

def get_planet_name(url:str) -> str:
    if not url:
        return 'Unknown'
    if url in PLANET_CACHE:
        print(f"беру из кеща {url}")
        return PLANET_CACHE[url]
    print(f"+++ Делаю запрос к API: {url}")
    try:
        res = requests.get(url, verify=False).json()
        planet_name = res['result']['properties']['name']
        #Сохраняем результат в кэш на будущее
        PLANET_CACHE[url] = planet_name
        return planet_name
    except Exception:
        return 'Unknown planet'

@app.get("/api/character/{char_id}", response_model=Person)
def get_person(person_id):
    person_url = f"https://swapi.tech/api/people/{person_id}/"
    response = requests.get(person_url, verify=False)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Character not found")

    person_data = response.json()['result']['properties']

    person_data['homeworld'] = get_planet_name(person_data['homeworld'])
    return Person(**person_data)

person = get_person(1)
person2 = get_person(3)
print(f"name : {person.name}, homeworld : {person.homeworld}")  #name : Luke Skywalker, homeworld : Tatooine
print(f"name : {person2.name}, homeworld : {person2.homeworld}")  #name : name : R2-D2, homeworld : Naboo

print(PLANET_CACHE)