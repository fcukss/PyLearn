import requests

import requests

import urllib3

# Отключаем предупреждение об отсутствии проверки (чтобы консоль была чистой)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_people():
    url = "https://swapi.tech/api/people/"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        return response.json()
    return {"error": response.status_code}

get_people()