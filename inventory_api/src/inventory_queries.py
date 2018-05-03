from beer import Beer
from filter_factory import build


def keep_requested_attributes(beer):
    return {key: beer[key] for key in ['name', 'size', 'category', 'price', 'quantity']}


def make_beer(beer):
    return Beer(beer['name'], beer['size'], beer['category'], beer['price'], beer['quantity'])


class InventoryQueries:

    def __init__(self, inventory):
        self.inventory = inventory

    def get_available_inventory(self):
        return [keep_requested_attributes(beer) for beer in
                self.inventory.get_historic_inventory_strings() if beer['quantity'] > 0]

    def get_filtered_inventory(self, filter_ds):
        beer_filter = build(filter_ds)
        return [beer for beer in self.inventory.get_historic_inventory()
                if beer_filter.is_match(beer)]
