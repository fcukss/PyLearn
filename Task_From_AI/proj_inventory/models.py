from datetime import date
from pydantic import BaseModel, Field

class Doctor(BaseModel):
    id: int
    name : str
    specialization : str


class MedicalItem(BaseModel):
    id: int  = Field(..., gt=0) #value must be >0
    name: str = Field(..., min_length=3)
    is_sterile: bool
    expire_date: date
    stock: int = Field(default=0, ge=0)  #ge=0 позволяет хранить 0 на складе
    price: float = Field(..., gt=0)
    created_by_doctor_id: int   # Это наш "внешний ключ" (ссылка на врача)

class Prescription(BaseModel):
    id: int
    doctor_id : int
    item_id : int
    patient_name: str