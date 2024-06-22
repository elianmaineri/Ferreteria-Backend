from Models.Productos import Productos as ProductosModel
from Schemas.ProductosSchemas import Productos


class ProductosService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_productos(self):
       productos = self.db.query(ProductosModel).all()
       return productos
    
    def get_id_productos(self, id:int):
        productos = self.db.query(ProductosModel).filter(ProductosModel.id == id).first()
        return productos
    
    def get_productos_categoria(self, categoria):
        productos = self.db.query(ProductosModel).filter(ProductosModel.categoria == categoria).all()
        return productos
    
    def create_productos(self, producto: Productos):
        new_producto = ProductosModel(**producto.dict())
        self.db.add(new_producto)
        self.db.commit()
        return
    
    def update_productos(self, id:int, data: Productos):
        productos = self.db.query(ProductosModel).filter(ProductosModel.id == id).first()
        productos.nombre = data.nombre
        productos.precio = data.precio
        productos.categoria = data.categoria
        self.db.commit()
        return
    
    def delete_productos(self, id:int):
        self.db.query(ProductosModel).filter(ProductosModel.id == id).delete()
        self.db.commit()
        return