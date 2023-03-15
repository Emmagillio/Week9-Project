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

# Create base model
class Sell(BaseModel):
    licence_number: str
    sold_date: str
    sold_price: int
    purchaser_fname: str
    purchaser_lname: str
    purchaser_phone: str
    purchaser_email: str


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


def validate_data(sell: Sell):
    valid = [
        sell.licence_number != "",
        sell.sold_date != "",
        type(sell.sold_price) == int,
    ]
