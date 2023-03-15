import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Car(Basemodel):
    make: str
    model: str
    colour: str
    year: str
    licence_number: str
    location: str
    bought_date: str
    bought_price: int
    seller_fname: str
    seller_lname: str
    seller_phone: str
    seller_email: str
    image_url: str

@app.post("/add_car")
def api_add_car(car: Car):
    