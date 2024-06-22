from pydantic import BaseModel, Field
from typing import Optional


class Ventas(BaseModel):

    id: int = Field(gt = 0)
    idUsuario: int = Field(gt = 0)
    idProducto: int = Field(gt = 0)
    cantidad: int = Field(gt = 0)
    estado: str
