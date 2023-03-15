import pymysql
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


class Car(BaseModel):
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

    if not validate_add_car_data(car):
        return {"message": "invalid data"}
    # generate sale price from bought price
    for_sale_price = for_sale_price(car.bought_price)

    # make a connection to the database
    con = pymysql.connect(
        host="localhost", user="root", password="password", database="dealer"
    )
    cur = con.cursor()

    sql = f"""insert into dealer(
        make, model, colour, year, licence_number, location, bought_date, bought_price, 
        for_sale_price, seller_fname, seller_lname, seller_phone, seller_email, image_url) 
        values('{car.make}', '{car.model}', '{car.colour}', '{car.year}', '{car.licence_number}', 
        '{car.location}', '{car.bought_date}', {car.bought_price}, {for_sale_price}, '{car.seller_fname}',
        '{car.seller_lname}', '{car.seller_phone}', '{car.seller_email}', '{car.image_url}')"""

    try:
        cur.execute(sql)
        con.commit()  #
    except:
        return {"message": "could not insert new data"}

    search = f"select id, make, model, colour, year, location, licence_number, for_sale_price, image_url from cars where licence_number like '%{car.licence_number}%'"
    cur.execute(search)
    res = cur.fetchone()

    # close the connection
    cur.close()
    con.close()

    new_car = {
        "Make": res[1],
        "Model": res[2],
        "Colour": res[3],
        "Year": res[4],
        "Location": res[5],
        "Licence Number": res[6],
        "Sale Price": res[7],
        "Image": res[8],
    }
    return new_car


def for_sale_price(bought_price):
    if bought_price:
        return int(bought_price * 1.5)


def validate_add_car_data(car):
    valid = [
        car.make != "",
        car.model != "",
        car.colour != "",
        car.year != "",
        car.licence_number != "",
        car.location != "",
        car.bought_date != "",
        type(car.bought_price) == type(int(1)) and car.bought_price >= 0,
        car.seller_fname != "",
        car.seller_lname != "",
        car.seller_phone != "",
        car.seller_email != "",
        car.image_url != "",
    ]

    if all(valid):
        return True
    else:
        return False
