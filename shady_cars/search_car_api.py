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
            and for_sale_price > {lower_price} and for_sale_price < {upper_price} order by for_sale_price DESC"

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
