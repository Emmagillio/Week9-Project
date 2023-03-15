from helpers import validate_sell_data, Sell

sell1 = Sell(
    licence_number="LG65 YHH",
    sold_date="06/11/2022  02:19:48",
    sold_price=22000,
    purchaser_fname="Saree",
    purchaser_lname="Stopps",
    purchaser_phone="299-207-9598",
    purchaser_email="sstopps0@state.gov",
)

sell2 = Sell(
    licence_number="",
    sold_date="06/11/2022  02:19:48",
    sold_price=22000,
    purchaser_fname="Saree",
    purchaser_lname="Stopps",
    purchaser_phone="299-207-9598",
    purchaser_email="sstopps0@state.gov",
)

sell3 = Sell(
    licence_number="LG65 YHH",
    sold_date="",
    sold_price=22000,
    purchaser_fname="Saree",
    purchaser_lname="Stopps",
    purchaser_phone="299-207-9598",
    purchaser_email="sstopps0@state.gov",
)

sell4 = Sell(
    licence_number="LG65 YHH",
    sold_date="06/11/2022  02:19:48",
    sold_price=-2345,
    purchaser_fname="Saree",
    purchaser_lname="Stopps",
    purchaser_phone="299-207-9598",
    purchaser_email="sstopps0@state.gov",
)

sell5 = Sell(
    licence_number="LG65 YHH",
    sold_date="06/11/2022  02:19:48",
    sold_price=-2345,
    purchaser_fname="",
    purchaser_lname="Stopps",
    purchaser_phone="299-207-9598",
    purchaser_email="sstopps0@state.gov",
)

sell6 = Sell(
    licence_number="LG65 YHH",
    sold_date="06/11/2022  02:19:48",
    sold_price=-2345,
    purchaser_fname="Saree",
    purchaser_lname="",
    purchaser_phone="299-207-9598",
    purchaser_email="sstopps0@state.gov",
)

sell7 = Sell(
    licence_number="LG65 YHH",
    sold_date="06/11/2022  02:19:48",
    sold_price=-2345,
    purchaser_fname="Saree",
    purchaser_lname="Stopps",
    purchaser_phone="",
    purchaser_email="sstopps0@state.gov",
)

sell8 = Sell(
    licence_number="LG65 YHH",
    sold_date="06/11/2022  02:19:48",
    sold_price=-2345,
    purchaser_fname="Saree",
    purchaser_lname="Stopps",
    purchaser_phone="299-207-9598",
    purchaser_email="",
)


def test_validate_sell_data():
    assert validate_sell_data(sell1) == True
    assert validate_sell_data(sell2) == False
    assert validate_sell_data(sell3) == False
    assert validate_sell_data(sell4) == False
    assert validate_sell_data(sell5) == False
    assert validate_sell_data(sell6) == False
    assert validate_sell_data(sell7) == False
    assert validate_sell_data(sell8) == False
