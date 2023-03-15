import sqlite3

con = sqlite3.connect("")
cur = con.cursor()


def search_all():
    cur.execute(
        "select make, model, colour, year, location, licence, for_sale_price, img_url from cars order by for_sale_price"
    )
