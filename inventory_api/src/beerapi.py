import json
from flask import Flask, request
from current_inventory import Inventory
from inventory_queries import InventoryQueries
from filter_ds import FilterDS
import most_recent_file
from style_db import StyleDB
from data_collector.src.file_location import FileLocation


APP = Flask(__name__)
QUERIES = None


def initialize_inventory():
    location = FileLocation.save_location
    the_file = most_recent_file.MostRecentFile(location)
    style = StyleDB()
    inventory = Inventory(the_file, style)
    global QUERIES
    QUERIES = InventoryQueries(inventory)


@APP.route('/current')
def get_current_inventory():
    keys = list(request.args.keys())
    for key in keys:
        if key != 'name' and key != 'size' and key != 'style' and key != 'availability':
            return "Bad parameter given!", 400

    name = request.args.get('name')
    size = request.args.get('size')
    style = request.args.get('style')
    availability = request.args.get('availability')

    beer_filter = FilterDS(name=name, size=size, style=style, availability=availability)
    beers = []
    filtered_inventory = QUERIES.get_filtered_inventory(beer_filter)
    if filtered_inventory:
        for beer in filtered_inventory:
            beers.append({'name': beer.name, 'size': beer.size, 'style': beer.style,
                          'quantity': beer.quantity, 'price': beer.price})
        return json.dumps(beers)
    return json.dumps([])


if __name__ == "__main__":
    initialize_inventory()
    APP.run(host="0.0.0.0", port=10000)