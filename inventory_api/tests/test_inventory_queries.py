from inventory_queries import InventoryQueries
from inventory import Inventory
from filter_ds import FilterDS

BASE_DIR = "inventory_api/tests/sample_csv_files/"


def make_test_inventory_query(test_file):
    test_file = test_file
    inventory = Inventory(BASE_DIR + test_file)
    return InventoryQueries(inventory)


def test_one_beer_name_filter_true():
    query = make_test_inventory_query("single_positive_quantity.csv")
    filter_ds = FilterDS(name="Bells Best Brown")
    assert query.get_filtered_inventory(filter_ds)[0].name == "Bells Best Brown"


def test_one_beer_name_filter_false():
    query = make_test_inventory_query("single_positive_quantity.csv")
    filter_ds = FilterDS(name="Guinness")
    assert not query.get_filtered_inventory(filter_ds)


def test_multiple_beers_name_filter_true():
    query = make_test_inventory_query("three.csv")
    filter_ds = FilterDS(name="Bells Best Brown")
    assert len(query.get_filtered_inventory(filter_ds)) == 1


def test_multiple_beers_name_filter_false():
    query = make_test_inventory_query("three.csv")
    filter_ds = FilterDS(name="Guinness")
    assert not query.get_filtered_inventory(filter_ds)
