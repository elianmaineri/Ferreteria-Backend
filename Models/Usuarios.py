from Config.database import Base
from sqlalchemy import Column, Integer, String, Float



class Usuarios(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key = True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    edad = Column(Integer)

    