from typing import Union

from fastapi import FastAPI

from datetime import date

import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/time")
def read_root():
    data_atual = date.today()
    return {"Data": data_atual}

@app.get("/dolar")
def read_root():
    return {"Dolar hoje:": "4,94 Real brasileiro"}

@app.get("/euro")
def read_root():
    return {"Euro hoje": "5,35 Real brasileiro"} 

@app.get("/random")
def read_root():
    numero = random.random()
    return {"Numero aleatorio: ": numero}    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}