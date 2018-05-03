from current_inventory import Inventory
import inventory_api.tests.mock_mostrecentfile as mostrecentfile
from inventory_api.tests.mock_brewery_db import MockBreweryDBStoutTracked


def inventory_has_proper_size_zero(size):
    tanczos_inventory = mostrecentfile.get_list_none()
    style_db = MockBreweryDBStoutTracked()

    i = Inventory(tanczos_inventory, style_db)
    assert size == len(i.get_historic_inventory())


def test_empty_inventory():
    inventory_has_proper_size_zero(0)


def inventory_has_proper_size_one(size):
    tanczos_inventory = mostrecentfile.get_list_one()
    style_db = MockBreweryDBStoutTracked()

    i = Inventory(tanczos_inventory, style_db)
    assert size == len(i.get_historic_inventory())


def test_single_list_inventory():
    inventory_has_proper_size_one(1)


def inventory_has_proper_size_three(size):
    tanczos_inventory = mostrecentfile.get_list_three()
    style_db = MockBreweryDBStoutTracked()

    i = Inventory(tanczos_inventory, style_db)
    assert size == len(i.get_historic_inventory())


def test_many_items():
    inventory_has_proper_size_three(3)


def test_correct_style_from_one_beer():
    tanczos_inventory = mostrecentfile.get_list_one()
    style_db = MockBreweryDBStoutTracked()

    i = Inventory(tanczos_inventory, style_db)
    values = i.get_historic_inventory()

    assert values[0].style == 'stout'
    assert values[0].name == 'BELLS BEST BROWN'


def test_correct_style_from_three_beers():
    tanczos_inventory = mostrecentfile.get_list_three()
    style_db = MockBreweryDBStoutTracked()

    i = Inventory(tanczos_inventory, style_db)
    values = i.get_historic_inventory()

    assert values[2].style == 'stout'
    assert values[2].name == 'GREAT LAKES OKTOBERFEST'
