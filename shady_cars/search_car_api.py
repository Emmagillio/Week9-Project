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
def search(search: str = ""):
    # Connect to database
    con = pymysql.connect(
        host="localhost", user="root", password="password", database="dealer"
    )
    cur = con.cursor()

    # Check for search query, create query to SQL database
    if search == "":
        query = "select id, make, model, colour, year, location, licence_number, for_sale_price, image_url from cars order by for_sale_price"
    else:
        query = f"select id, make, model, colour, year, location, licence_number, for_sale_price, image_url from cars where licence_number like '%{search}%' order by for_sale_price"

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
        cars.append(car_result)

    # Check for any returned results and return
    if cars:
        return cars
    else:
        return "No results found"
