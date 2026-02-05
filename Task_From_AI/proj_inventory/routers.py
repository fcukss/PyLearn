from fastapi import HTTPException
from fastapi.params import Depends

from models import Prescription, MedicalItem
from database import db_prescriptions,db_doctors,db_items
from typing import Literal

from fastapi import APIRouter

from auth_logic import get_current_user

router = APIRouter()

"""Создай два эндпоинта:

POST /med-items/ — принимает модель MedicalItem 
и сохраняет её через твой класс-менеджер.

DELETE /med-items/{item_id} — вызывает метод удаления 
из твоего класса-менеджера."""

@router.post('/med-items')
def create_item(item: MedicalItem):
    data = db_items.load()
    for i in data:
        if i['id'] == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    data.append(item.model_dump())
    db_items.save(data)
    return {"message": "Item added", "item": item}
@router.delete("/med-items/{item_id}")
def delete_item(item_id:int):
    success = db_items.delete(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Item {item_id} deleted"}
@router.patch('/med-items/{item_id}/update-stock')
def patch_item(item_id, amount:int):
    data = db_items.load()
    found = False
    updated_item = None
    for item in data:
        if item['id'] == item_id:
            new_stock = item['stock'] + amount
            if new_stock < 0:
                raise HTTPException(status_code=400, detail="Stock cannot be negative")
            item['stock'] = new_stock
            found = True
            updated_item = item
            break
    if not found:
        raise HTTPException(status_code=404, detail="Item not found")
    db_items.save(data)
    return {"message": "Stock updated", "item": updated_item}
@router.get('/med-items/sterile')
def get_sterile():
    data = db_items.load()
    return [i for i in data if i.get('is_sterile')]

@router.get('/med-items/stats')
def get_stats():
    data = db_items.load()

    total_items = len(data)
    total_stock = 0
    total_value = 0
    sterile_count = 0

    for item in data:
        stock = item.get('stock', 0)
        price = item.get('price', 0.0)

        total_stock += stock
        total_value += stock * price

        if item.get('is_sterile'):
            sterile_count += 1

    return {
        'total_items' : total_items,
        'total_stock' : total_stock,
        'total_value' : round(total_value,2),  #Округляем до центов
        'sterile_percentage' :  sterile_count /total_items * 100 if total_items > 0 else 0.0
    }
"""Сортировка и валидация параметров"""
@router.get('/med-items/')
#В переменную sort_by можно положить либо строку из списка Literal, ЛИБО ничего (None)
def get_items(sort_by : Literal['name', 'price', 'stock'] | None = None,
              reverse: bool = False):

    data = db_items.load()
    if sort_by:
        ## Так как мы использовали Literal, FastAPI пропустит сюда только
        # разрешенные строки. Нам остается только вызвать sorted.
        data = sorted(data, key=lambda x: x.get(sort_by), reverse=reverse)
    return data

@router.get('/med-items/full-info/{item_id}')
def get_full_item_info(item_id:int):
    items  = db_items.load()
    doctors = db_doctors.load()

    # find item for id
    item = next((i for i in items if i['id']==item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')

    #find doctor r by id in the item
    doctor_id = item.get('created_by_doctor_id')
    doctor = next((d for d in doctors if d['id']==doctor_id), None)

    #create full result
    full_info = item.copy()
    full_info['doctor_details'] = doctor if doctor else 'Doctor not found'

    return full_info

@router.get('/doctors/{doctor_id}/items')
def get_doctors_item_info(doctor_id:int):
    items = db_items.load()
    doctors = db_doctors.load()
    doctor = next((d for d in doctors if d['id'] == doctor_id), None)
    if not doctor:
        raise HTTPException(status_code=404, detail='Doctor not found')
    data = [i['name'] for i in items if i['created_by_doctor_id']==doctor_id]
    return {
        'doctor_bane': doctor['name'],
        'items_created' : data
    }
@router.post('/prescriptions/')
def create_prescription(
        prescription: Prescription,
        current_user: dict = Depends(get_current_user)
):
    items = db_items.load()
    doctors = db_doctors.load()
    current_prescriptions = db_prescriptions.load()

    print(f"ЗАГРУЖЕННЫЕ ПРЕДМЕТЫ: {items}")

    if any(p['id']==prescription.id for p in current_prescriptions):
        raise HTTPException(status_code=400, detail='Prescription ID already exists')

    doctor = next((d for d in doctors if d['id'] == prescription.doctor_id), None)
    if not doctor:
        raise HTTPException(status_code=404, detail='Doctor not found')

    item = next((i for i in items if i['id']==prescription.item_id),None)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')

    if item['stock']<=0:
        raise  HTTPException(status_code=400, detail='Item not in stock')

    item['stock']-=1
    db_items.save(items)

    current_prescriptions.append(prescription.model_dump())
    db_prescriptions.save(current_prescriptions)
    return {"message": "Prescription created",
            "remaining_stock": item['stock'],
            "doctor_acting": current_user["username"]}
