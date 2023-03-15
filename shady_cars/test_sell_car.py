from helpers import validate_sell_data, Sell

sell1 = Sell(licence_number="LG65 YHH", sold_date="06/11/2022  02:19:48", s)


def test_validate_sell_data():
    assert validate_sell_data(sell1) == True
