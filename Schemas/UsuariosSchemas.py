from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Usuarios(BaseModel):
    id: int = Field(gt = 0)
    nombre: str
    apellido: str
    email: EmailStr
    password: str = Field(min_length=8)
    edad: int
