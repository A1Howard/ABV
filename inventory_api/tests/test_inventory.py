import pytest
from inventory import Inventory

BASE_DIR = 'inventory_api/tests/sample_csv_files/'


def inventory_has_proper_size(filename, size):
    i = Inventory(BASE_DIR + filename)
    assert size == len(i.get_historic_inventory())


def test_empty_inventory():
    inventory_has_proper_size('empty.csv', 0)


def test_single_item_inventory():
    inventory_has_proper_size('single.csv', 1)


def test_many_items():
    inventory_has_proper_size('three.csv', 3)


def test_load_numeric_fields():
    i = Inventory(BASE_DIR + 'single.csv')
    values = i.get_historic_inventory_strings()[0]
    assert pytest.approx(0) == values['quantity']
    assert pytest.approx(182.99) == values['price']
    assert pytest.approx(182.99) == values['case_price']
    assert pytest.approx(1) == values['case_pack']


def test_load_convert_case():
    i = Inventory(BASE_DIR + 'single.csv')
    values = i.get_historic_inventory_strings()[0]
    assert values['name'] == 'Bells Best Brown'
    assert values['size'] == '1/2 Keg'
    assert values['category'] == 'Craft'
