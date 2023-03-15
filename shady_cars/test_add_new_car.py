from helpers import validate_add_car_data, Car, for_sale_price


car1 = Car(
    make="VW",
    model="golf",
    colour="black",
    year="2001",
    licence_number="AB61 CDE",
    location="London",
    bought_date="2022-07-24 00:41:47",
    bought_price=18386,
    seller_fname="Elston",
    seller_lname="Backshell",
    seller_phone="453-275-4832",
    seller_email="ebackshell0@arizona.edu",
    image_url="http://dummyimage.com/200x200.png/cc0000/ffffff",
)
car2 = Car(
    make="",
    model="golf",
    colour="black",
    year="2001",
    licence_number="AB61 CDE",
    location="London",
    bought_date="2022-07-24 00:41:47",
    bought_price=18386,
    seller_fname="Elston",
    seller_lname="Backshell",
    seller_phone="453-275-4832",
    seller_email="ebackshell0@arizona.edu",
    image_url="http://dummyimage.com/200x200.png/cc0000/ffffff",
)
car3 = Car(
    make="VW",
    model="golf",
    colour="black",
    year="2001",
    licence_number="AB61 CDE",
    location="London",
    bought_date="2022-07-24 00:41:47",
    bought_price=-1,
    seller_fname="Elston",
    seller_lname="Backshell",
    seller_phone="453-275-4832",
    seller_email="ebackshell0@arizona.edu",
    image_url="http://dummyimage.com/200x200.png/cc0000/ffffff",
)
car4 = Car(
    make="VW",
    model="golf",
    colour="black",
    year="2001",
    licence_number="AB61 CDE",
    location="London",
    bought_date="2022-07-24 00:41:47",
    bought_price=18386,
    seller_fname="Elston",
    seller_lname="Backshell",
    seller_phone="453-275-4832",
    seller_email="ebackshell0@arizona.edu",
    image_url="",
)
car5 = Car(
    make="VW",
    model="golf",
    colour="black",
    year="2001",
    licence_number="AB61 CDE",
    location="London",
    bought_date="",
    bought_price=18386,
    seller_fname="Elston",
    seller_lname="Backshell",
    seller_phone="453-275-4832",
    seller_email="ebackshell0@arizona.edu",
    image_url="http://dummyimage.com/200x200.png/cc0000/ffffff",
)


def test_validate_data():
    assert validate_add_car_data(car1) == True
    assert validate_add_car_data(car2) == False
    assert validate_add_car_data(car3) == False
    assert validate_add_car_data(car4) == False
    assert validate_add_car_data(car4) == False


def test_sql_insert_statement():
    car = car1
    forsale_price = for_sale_price(car.bought_price)
    assert (
        f"""insert into dealer(
        make, model, colour, year, licence_number, location, bought_date, bought_price, 
        for_sale_price, seller_fname, seller_lname, seller_phone, seller_email, image_url) 
        values('{car.make}', '{car.model}', '{car.colour}', '{car.year}', '{car.licence_number}', 
        '{car.location}', '{car.bought_date}', {car.bought_price}, {forsale_price}, '{car.seller_fname}',
        '{car.seller_lname}', '{car.seller_phone}', '{car.seller_email}', '{car.image_url}')"""
        == """insert into dealer(
        make, model, colour, year, licence_number, location, bought_date, bought_price, 
        for_sale_price, seller_fname, seller_lname, seller_phone, seller_email, image_url) 
        values('VW', 'golf', 'black', '2001', 'AB61 CDE', 
        'London', '2022-07-24 00:41:47', 18386, 18386, 'Elston',
        'Backshell', '453-275-4832', 'ebackshell0@arizona.edu', 'http://dummyimage.com/200x200.png/cc0000/ffffff')"""
    )
