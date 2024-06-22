from Config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Productos(Base):

    __tablename__ = "productos"

    id = Column(Integer, primary_key = True)
    nombre = Column(String(50))
    precio = Column(Float)
    categoria = Column(String(50))
    descripcion = Column(String(250))
