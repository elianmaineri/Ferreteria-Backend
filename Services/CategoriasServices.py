from Models.Categorias import Categorias as CategoriasModel
from Schemas.CategoriasSchemas import Categorias


class CategoriasService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_categorias(self):
        categoria = self.db.query(CategoriasModel).all()
        return categoria
    
    def get_id_categorias(self, id):
        categoria = self.db.query(CategoriasModel).filter(CategoriasModel.id == id).first()
        return categoria

    def create_categorias(self, Categorias: Categorias):
        new_categoria = CategoriasModel(**Categorias.dict())
        self.db.add(new_categoria)
        self.db.commit()
        return
    
    def update_categorias(self, id: int, data: Categorias):
        categoria = self.db.query(CategoriasModel).filter(CategoriasModel.id == id).first()
        categoria.nombre = data.nombre
        self.db.commit()
        return
    
    def delete_categorias(self, id: int):
        self.db.query(CategoriasModel).filter(CategoriasModel.id == id).delete()
        self.db.commit()
        return
    

    
