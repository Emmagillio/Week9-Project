def test_search_sql():
    licence_number = "LG65 YHH"
    make = "Ford"
    colour = "Red"
    lower_price = 500
    upper_price = 20000

    assert (
        f"select id, make, model, colour, year, location, licence_number, for_sale_price, image_url from \
            cars where licence_number like '%{licence_number}%' and make like '%{make}%' and colour like '%{colour}%' \
            and for_sale_price > {lower_price} and for_sale_price < {upper_price} order by for_sale_price"
        == "select id, make, model, colour, year, location, licence_number, for_sale_price, image_url from \
            cars where licence_number like '%LG65 YHH%' and make like '%Ford%' and colour like '%Red%' \
            and for_sale_price > 500 and for_sale_price < 20000 order by for_sale_price"
    )
