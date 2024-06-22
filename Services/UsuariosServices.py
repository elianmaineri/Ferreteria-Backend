from Models.Usuarios import Usuarios as UsuariosModel
from Schemas.UsuariosSchemas import Usuarios


class UsuariosService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_usuarios(self):
        usuarios = self.db.query(UsuariosModel).all()
        return usuarios
    
    def get_id_usuarios(self, id:int):
        usuarios = self.db.query(UsuariosModel).filter(UsuariosModel.id == id).first()
        return usuarios
    
    def get_email_usuarios(self, email:str):
        usuarios = self.db.query(UsuariosModel).filter(UsuariosModel.email == email).first()
        return usuarios
    
    def create_usuarios(self, usuario:Usuarios):
        new_usuario = UsuariosModel(**usuario.dict())
        self.db.add(new_usuario)
        self.db.commit()
        return
    
    def update_usuarios(self, id:int, data: Usuarios):
        usuarios = self.db.query(UsuariosModel).filter(UsuariosModel.id == id).first()
        usuarios.nombre = data.nombre
        usuarios.apellido = data.apellido
        usuarios.email = data.email
        usuarios.password = data.password
        usuarios.edad = data.edad
        self.db.commit()
        return
    
    def delete_usuarios(self, id:int):
        self.db.query(UsuariosModel).filter(UsuariosModel.id == id).delete()
        self.db.commit()