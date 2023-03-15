from helpers import validate_add_car_data, Car


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
