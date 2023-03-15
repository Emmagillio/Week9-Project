from pydantic import BaseModel


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


def validate_sell_data(sell: Sell):
    valid = [
        sell.licence_number != "",
        sell.sold_date != "",
        isinstance(sell.sold_price, int),
        sell.sold_price >= 0,
        sell.purchaser_fname != "",
        sell.purchaser_lname != "",
        sell.purchaser_phone != "",
        sell.purchaser_email != "",
    ]

    if all(valid):
        return True
    else:
        return False
