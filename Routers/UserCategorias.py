from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from Config.database import Session
from Models.Categorias import Categorias as CategoriaModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from Services.CategoriasServices import CategoriasService
from Schemas.CategoriasSchemas import Categorias

categorias_router = APIRouter()

@categorias_router.get('/ALL-CATEGORIAS', tags=['Categorias'], response_model=List[Categorias], status_code=200, dependencies=[Depends(JWTBearer())])
def get_all_categorias() -> List[Categorias]:
    db = Session()
    categorias = CategoriasService(db).get_all_categorias()
    return JSONResponse(status_code=200, content=jsonable_encoder(categorias))

@categorias_router.get('/ID-CATEGORIAsS', tags=['Categorias'], response_model=Categorias)
def get_id_categorias(id: int):
    db = Session()
    categoriasId = CategoriasService(db).get_id_categorias(id)
    if not categoriasId:
        return JSONResponse(status_code=404, content={"message": "Categoria no encontrada"})
    return JSONResponse(status_code=200, content=jsonable_encoder(categoriasId))

@categorias_router.post('/CATEGORIAS', tags=['Categorias'], response_model=dict, status_code=201)
def create_categorias(categoria: Categorias) -> dict:
    db = Session()
    CategoriasService(db).create_categorias(categoria)
    return JSONResponse(status_code=200, content={"message" : "Categoria registrada con exito"})


@categorias_router.put('/CATEGORIAS', tags=['Categorias'], response_model=dict, status_code=200)
def update_categorias(id:int, categoria: Categorias) -> dict:
    db = Session()
    categoriaId = CategoriasService(db).get_id_categorias(id)
    if not categoriaId:
        return JSONResponse(status_code=404, content={"message": "Categoria no encontrada"})
    CategoriasService(db).update_categorias(id, categoria)
    return JSONResponse(status_code=200, content={"message": "Categoria modificada con exito"})

@categorias_router.delete('/CATEGORIAS', tags=['Categorias'], response_model=dict, status_code=200)
def delete_categorias(id:int) -> dict:
    db = Session()
    categoriaId = CategoriasService(db).get_id_categorias(id)
    if not categoriaId:
        return JSONResponse(status_code=404, content={"message": "Categoria no encontrada"})
    CategoriasService(db).delete_categorias(id)
    return JSONResponse(status_code=200, content={"message": "Categoria eliminada con exito"}) 



