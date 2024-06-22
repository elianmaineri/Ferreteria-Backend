from Models.Ventas import Ventas as VentasModel
from Schemas.VentasSchemas import Ventas


class VentasService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_ventas(self):
        ventas = self.db.query(VentasModel).all()
        return ventas
    
    def get_id_ventas(self, id:int):
        ventas = self.db.query(VentasModel).filter(VentasModel.id == id).first()
        return ventas
    
    def get_estado_ventas(self, estado:str):
        ventas = self.db.query(VentasModel).filter(VentasModel.estado == estado).first()
        return ventas
    
    def create_ventas(self, venta:Ventas):
        new_venta = VentasModel(**venta.dict())
        self.db.add(new_venta)
        self.db.commit()
        return
    
    def update_ventas(self, id:int, data: Ventas):
        ventas = self.db.query(VentasModel).filter(VentasModel.id == id).first()
        ventas.idUsuario = data.idUsuario
        ventas.idProducto = data.idProducto
        ventas.cantidad = data.cantidad
        ventas.estado = data.estado
        self.db.commit()
        return
    
    def delete_ventas(self, id:int):
        self.db.query(VentasModel).filter(VentasModel.id == id).delete()
        self.db.commit()
        return