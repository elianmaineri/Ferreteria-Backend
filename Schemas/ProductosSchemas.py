from pydantic import BaseModel, Field
from typing import Optional


class Productos(BaseModel):
    id: int = Field(gt = 0)
    nombre: str
    precio: int
    categoria: str  
    descripcion: str