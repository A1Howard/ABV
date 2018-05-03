from beer import Beer
from filter_ds import FilterDS
from filter_factory import build


def test_all_attributes_match():
    test_beer = Beer("Guinness", "12/12 OZ. BTL", "Stout", "30.00", 2)
    test_ds = FilterDS("12/12 OZ. BTL", "Stout", "Guinness", 2)
    test_filter = build(test_ds)
    assert test_filter.is_match(test_beer) is True


def test_attribute_mismatch_fails():
    test_beer = Beer("Guinness", "12/12 OZ. BTL", "Stout", "30.00", 2)
    test_ds = FilterDS("24/12 OZ. CAN", "College", "Natty Light", 0)
    test_filter = build(test_ds)
    assert test_filter.is_match(test_beer) is False
