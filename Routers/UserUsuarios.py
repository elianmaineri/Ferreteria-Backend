from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from Config.database import Session
from Models.Usuarios import Usuarios as UsuariosModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from Services.UsuariosServices import UsuariosService
from Schemas.UsuariosSchemas import Usuarios


usuarios_router = APIRouter()

@usuarios_router.get('/ALL-USUARIOS', tags=['Usuarios'], response_model=List[Usuarios], dependencies=[Depends(JWTBearer())])
def get_all_usuarios() -> List:
    db = Session()
    usuariosAll = UsuariosService(db).get_all_usuarios()
    if not usuariosAll:
        return JSONResponse(status_code=404, content={"message": "No hay usuarios registrados"})
    return JSONResponse(status_code=200, content=jsonable_encoder(usuariosAll))

@usuarios_router.get('/ID-USUARIOS', tags=['Usuarios'], response_model=Usuarios)
def get_id_usuarios(id: int):
    db = Session()
    usuariosId = UsuariosService(db).get_id_usuarios(id)
    if not usuariosId:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontrado con exito"})
    return JSONResponse(status_code=200, content=jsonable_encoder(usuariosId))

@usuarios_router.get('/EMAIL-USUARIOS', tags=['Usuarios'], response_model=Usuarios)
def get_email_usuarios(email: str):
    db = Session()
    usuariosEmail = UsuariosService(db).get_email_usuarios(email)
    if not usuariosEmail:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontrado con exito"})
    return JSONResponse(status_code=200, content=jsonable_encoder(usuariosEmail))

@usuarios_router.post('/USUARIOS', tags=['Usuarios'], response_model=Usuarios)
def create_usuarios(usuario: Usuarios):
    db = Session()
    UsuariosService(db).create_usuarios(usuario)
    return JSONResponse(status_code=200, content={"message": "Usuario creado con exito"})

@usuarios_router.put('/USUARIOS', tags=['Usuarios'], response_model=Usuarios)
def update_usuarios(id: int, usuario: Usuarios):
    db = Session()
    usuarioId = UsuariosService(db).get_id_usuarios(id)
    if not usuarioId:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontrado con exito"})
    UsuariosService(db).update_usuarios(id, usuario)
    return JSONResponse(status_code=200, content={"message": "Usuario modificado con exito"})

@usuarios_router.delete('/USUARIOS', tags=['Usuarios'], response_model=Usuarios)
def delete_usuarios(id: int):
    db = Session()
    usuarioId = UsuariosService(db).get_id_usuarios(id)
    if not usuarioId:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontrado con exito"})
    UsuariosService(db).delete_usuarios(id)
    return JSONResponse(status_code=200, content={"message": "Usuario eliminado con exito"})





