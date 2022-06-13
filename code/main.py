from fastapi import FastAPI

import sqlite3 
# Permite generar una lista
from typing import List
# Permite validar 
from pydantic import BaseModel

class Respuesta(BaseModel):
    message: str

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str

app = FastAPI()


@app.get("/", response_model=Respuesta)
async def index():
    return {"message": "API REST"}

@app.get("/clientes/", response_model=List[Cliente])
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response = cursor.fetchall()
        return response 

@app.get("/clientes/{id}", response_model=List[Cliente])
async def clientes(id: int):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory=sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes where id_cliente={}".format(int(id)))
        response = cursor.fetchall()
        return response