from inventory_queries import InventoryQueries
from inventory import Inventory

BASE_DIR = 'inventory_api/tests/sample_csv_files/'


def make_beer(quantity):
    return {'name': 'Bells Best Brown',
            'size': '1/2 Keg',
            'category': 'Craft',
            'quantity': quantity,
            'price': 182.99}


def make_queries(filename):
    return InventoryQueries(Inventory(BASE_DIR + filename))


def test_no_inventory():
    queries = make_queries('empty.csv')
    assert [] == queries.get_available_inventory()


def test_single_item_with_positive_quantity():
    expected = [make_beer(1)]
    queries = make_queries('single_positive_quantity.csv')
    assert expected == queries.get_available_inventory()


def test_single_item_with_zero_quantity():
    queries = make_queries('single_zero_quantity.csv')
    assert [] == queries.get_available_inventory()


def test_single_item_with_negative_quantity():
    queries = make_queries('single_negative_quantity.csv')
    assert [] == queries.get_available_inventory()
