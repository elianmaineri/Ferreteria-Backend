from pydantic import BaseModel, Field
from typing import Optional


class Categorias(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=5, max_length=20)


