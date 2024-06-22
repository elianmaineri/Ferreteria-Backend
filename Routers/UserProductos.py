from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from Config.database import Session
from Models.Productos import Productos as ProductosModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from Services.ProductosServices import ProductosService
from Schemas.ProductosSchemas import Productos


productos_router = APIRouter()

@productos_router.get('/ALL-PRODUCTOS', tags=['Productos'], response_model=List[Productos], status_code=200)
def get_all_productos() -> List[Productos]:
    db = Session()
    productos = ProductosService(db).get_all_productos()
    return JSONResponse(status_code=200, content=jsonable_encoder(productos))

@productos_router.get('/ID-PRODUCTOS', tags=['Productos'], response_model=Productos, status_code=200)
def get_id_productos(id: int):
    db = Session()
    productos = ProductosService(db).get_id_productos(id)
    if not productos:
        return JSONResponse(status_code=404, content={"message":"Prodcutos no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(productos))

@productos_router.get('/CAT-PRODUCTOS', tags=['Productos'], response_model=Productos, status_code=200)
def get_categoria_productos(categoria: str):
    db = Session()
    productos = ProductosService(db).get_productos_categoria(categoria)
    if not productos:
        return JSONResponse(status_code=404, content={"message":"Producto no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(productos))

@productos_router.post('/PRODUCTOS', tags=['Productos'], response_model=Productos)
def create_productos(producto:Productos):
    db = Session()
    ProductosService(db).create_productos(producto)
    return JSONResponse(status_code=200, content={"message":"Producto creado con exito"})

@productos_router.put('/PRODUCTOS', tags=['Productos'], response_model=Productos)
def update_productos(id:int, producto: Productos):
    db = Session()
    productoId = ProductosService(db).get_id_productos(id)
    if not productoId:
        return JSONResponse(status_code=404, content={"message": "Producto no encontrado"})
    ProductosService(db).update_productos(id, producto)
    return JSONResponse(status_code=200, content={"message": "Producto modificado con exito"})

@productos_router.delete('/PRODUCTOS', tags=['Productos'], response_model=Productos)
def delete_productos(id: int):
    db = Session()
    productoId = ProductosService(db).get_id_productos(id)
    if not productoId:
        return JSONResponse(status_code=404, content={"message":"Producto no encontrado"})
    ProductosService(db).delete_productos(id)
    return JSONResponse(status_code=200, content={"message":"Producto eliminado con exito"})



