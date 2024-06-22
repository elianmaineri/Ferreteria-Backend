from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from Config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from Routers.UserProductos import productos_router
from Routers.UserCategorias import categorias_router
from Routers.UserUsuarios import usuarios_router
from Routers.UserVentas import ventas_router

app = FastAPI()
app.title = "Ferreteria"
app.version = "0.0.1"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"], 
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

#app.add_middleware(ErrorHandler)
app.include_router(productos_router)
app.include_router(categorias_router)
app.include_router(usuarios_router)
app.include_router(ventas_router)


Base.metadata.create_all(bind=engine)