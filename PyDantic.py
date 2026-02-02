from pydantic import BaseModel
from typing import Optional   # импортируется в случае, если атрибут нужно сделать опциональным

class Person(BaseModel):
    name: str
    height: float
    mass: int
    gender: Optional[str] = None

person = Person(name='Harry', height=178.9, mass=90)
print(person)

print(f'{person.gender}')