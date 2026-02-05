from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
def test_read_stats():
    response = client.get("/api/v1/med-items/stats")

    assert response.status_code == 200
    data = response.json()
    assert 'total_items' in data
    assert 'total_value' in data
    assert isinstance(data['total_stock'],int)

def test_get_nonexistant_doctor():
    response = client.get("/api/v1/doctors/99999/items")
    assert response.status_code == 404

def test_create_prescription_unauthorized():
    # Пытаемся создать рецепт без заголовка Authorization
    payload = {
        "id": 999,
        "doctor_id": 1,
        "item_id": 101,
        "date": "2026-02-04"
    }
    response = client.post("/api/v1/prescriptions/", json=payload)
    assert response.status_code==401

def test_create_prescription_authorized():
    payload = {
            "id": 888,
            "doctor_id": 1,
            "item_id": 101,
            "date": "2026-02-04",
        "patient_name": "James Bond"
    }
    # Добавляем заголовок с нашим "секретным" токеном
    headers = {"Authorization": "Bearer secret_token_house"}
    response = client.post("/api/v1/prescriptions/", json=payload, headers=headers)
    if response.status_code == 404:
        print(f"\nОШИБКА ВАЛИДАЦИИ: {response.json()}")
    assert response.status_code == 200  # Теперь должно пройти

def test_debug_routes():
    # Печатаем все пути, которые видит наше приложение
    for route in app.routes:
        print(f"Путь: {route.path} | Методы: {route.methods}")