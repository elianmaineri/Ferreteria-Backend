from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from Config.database import Session
from Models.Ventas import Ventas as VentasModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from Services.VentasServices import VentasService
from Schemas.VentasSchemas import Ventas


ventas_router = APIRouter()

@ventas_router.get('/ALL-VENTAS', tags=['Ventas'], response_model=List[Ventas], dependencies=[Depends(JWTBearer())])
def get_all_ventas() -> List:
    db = Session()
    ventasAll = VentasService(db).get_all_ventas()
    if not ventasAll:
        return JSONResponse(status_code=404, content={"message": "No hay ninguna venta registrada"})
    return JSONResponse(status_code=200, content=jsonable_encoder(ventasAll))

@ventas_router.get('/ID-VENTAS', tags=['Ventas'], response_model=Ventas)
def get_id_ventas(id: int):
    db = Session()
    ventasId = VentasService(db).get_id_ventas(id)
    if not ventasId:
        return JSONResponse(status_code=404, content={"message": "Venta no encontrada con exito"})
    return JSONResponse(status_code=200, content=jsonable_encoder(ventasId))

@ventas_router.get('/ESTADO-VENTAS', tags=['Ventas'], response_model=Ventas)
def get_estado_ventas(estado: str):
    db = Session()
    ventasEstado = VentasService(db).get_estado_ventas(estado)
    if not ventasEstado:
        return JSONResponse(status_code=404, content={"message": "No se encontraron ventas con ese estado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(ventasEstado))

@ventas_router.post('/VENTAS', tags=['Ventas'], response_model=Ventas)
def create_ventas(venta: Ventas):
    db = Session()
    VentasService(db).create_ventas(venta)
    return JSONResponse(status_code=200, content={"message": "Venta creada con exito"})


@ventas_router.put('/VENTAS', tags=['Ventas'], response_model=Ventas)
def update_ventas(id: int, venta: Ventas):
    db = Session()
    ventaId = VentasService(db).get_id_ventas(id)
    if not ventaId:
        return JSONResponse(status_code=404, content={"message": "Venta no encontrada"})
    VentasService(db).update_ventas(id, venta)
    return JSONResponse(status_code=200, content={"message": "Venta modificada con exito"})

@ventas_router.delete('/VENTAS', tags=['Ventas'], response_model=Ventas)
def delete_ventas(id: int):
    db = Session()
    ventaId = VentasService(db).get_id_ventas(id)
    if not ventaId:
        return JSONResponse(status_code=404, content={"message": "Venta no encontrada"})
    VentasService(db).delete_ventas(id)
    return JSONResponse(status_code=200, content={"message": "Venta eliminada con exito"})