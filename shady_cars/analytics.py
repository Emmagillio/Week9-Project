import pymysql
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/analytics")
def search_sold():
    # Connect to database
    con = pymysql.connect(
        host="localhost", user="root", password="password", database="dealer"
    )
    cur = con.cursor()

    query = f"select id, licence_number, bought_price, for_sale_price, sold_price, sold_date from cars where sold_date IS NOT NULL"

    cur.execute(query)

    res = cur.fetchall()

    # Close database connections
    cur.close()
    con.close()

    sold = {}

    for car in res:
        car_result = {
            car[0]: {
                "Licence Number": car[1],
                "Bought Price": car[2],
                "Sale Price": car[3],
                "Sold Price": car[4],
                "Sold Date": car[5],
            }
        }
        sold.update(car_result)

    if sold:
        return sold
    else:
        return "No results found"
