import pymysql
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from helpers import Car, Sell, validate_add_car_data, validate_sell_data, for_sale_price


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


class Sell(BaseModel):
    licence_number: str
    sold_date: str
    sold_price: int
    purchaser_fname: str
    purchaser_lname: str
    purchaser_phone: str
    purchaser_email: str


@app.post("/add_car")
def api_add_car(car: Car):

    if not validate_add_car_data(car):
        return {"message": "invalid data"}
    # generate sale price from bought price
    forsale_price = for_sale_price(car.bought_price)

    # make a connection to the database
    con = pymysql.connect(
        host="localhost", user="root", password="password", database="dealer"
    )
    cur = con.cursor()

    sql = f"""insert into dealer(
        make, model, colour, year, licence_number, location, bought_date, bought_price, 
        for_sale_price, seller_fname, seller_lname, seller_phone, seller_email, image_url) 
        values('{car.make}', '{car.model}', '{car.colour}', '{car.year}', '{car.licence_number}', 
        '{car.location}', '{car.bought_date}', {car.bought_price}, {forsale_price}, '{car.seller_fname}',
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


@app.get("/cars")
def search(
    licence_number: str = "",
    make: str = "",
    colour: str = "",
    lower_price: int = -1,
    upper_price: int = 9999999,
):
    # Connect to database
    con = pymysql.connect(
        host="localhost", user="root", password="password", database="dealer"
    )
    cur = con.cursor()

    # Check for search query, create query to SQL database
    query = f"select id, make, model, colour, year, location, licence_number, for_sale_price, image_url from \
            cars where licence_number like '%{licence_number}%' and make like '%{make}%' and colour like '%{colour}%' \
            and for_sale_price > {lower_price} and for_sale_price < {upper_price} order by for_sale_price"

    # Execute query and fetch results
    cur.execute(query)
    res = cur.fetchall()

    # Close database connections
    cur.close()
    con.close()

    # Initialize results dictionary
    cars = {}

    # Iterate through SQL query results and append JSON to dictionary
    for car in res:
        car_result = {
            car[0]: {
                "Make": car[1],
                "Model": car[2],
                "Colour": car[3],
                "Year": car[4],
                "Location": car[5],
                "Licence Number": car[6],
                "Sale Price": car[7],
                "Image": car[8],
            }
        }
        cars.update(car_result)

    # Check for any returned results and return
    if cars:
        return cars
    else:
        return "No results found"


@app.put("/sell")
def sell_car(sell: Sell):
    # Connect to database
    con = pymysql.connect(
        host="localhost", user="root", password="password", database="dealer"
    )
    cur = con.cursor()

    # Create query to SQL database
    query = f"update cars set sold_date = {sell.sold_date}, sold_price = {sell.sold_price}, purchaser_fname = {sell.purchaser_fname}, \
            purchaser_lname = {sell.purchaser_lname}, purchaser_phone = {sell.purchaser_phone}, purchaser_email = {sell.purchaser_email} \
            where licence_number = {sell.licence_number}"

    # Execute query
    cur.execute(query)

    # Commit changes
    con.commit()

    # Close connection
    cur.close()
    con.close()
