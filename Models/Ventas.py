from Config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Ventas(Base):

    __tablename__ = "ventas"

    id = Column(Integer, primary_key = True)
    idUsuario = Column(Integer)
    idProducto = Column(Integer)
    cantidad = Column(Integer)
    estado = Column(String(30))
