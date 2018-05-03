from beer import Beer


def test_beer_attributes():
    beer_attribute = Beer("Guinness", "12/12 OZ. BTL", "Stout", "2", "30.00")
    assert beer_attribute.name == "Guinness"
    assert beer_attribute.size == "12/12 OZ. BTL"
    assert beer_attribute.style == "Stout"
    assert beer_attribute.price == "30.00"
    assert beer_attribute.quantity == "2"
    assert beer_attribute.is_available() is True


def test_non_available_beer():
    non_beer = Beer("Natty Light", "24/12 OZ. CAN", "College", "0", "20.00")
    assert non_beer.is_available() is False
    assert non_beer.quantity == "0"


def test_negative_quantity_beer():
    negative_beer = Beer("Lionshead", "24/12 OZ. CAN", "Pilsner", "-1", "30.00")
    assert negative_beer.is_available() is False
    assert negative_beer.quantity == "-1"
