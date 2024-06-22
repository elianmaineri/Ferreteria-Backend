from Config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Categorias(Base):

    __tablename__ = "categorias"

    id = Column(Integer, primary_key = True)
    nombre = Column(String(20))