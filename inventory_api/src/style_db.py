# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from brewerydb_queries import BreweryDBQueries
from style_cache import StyleCache


class StyleDB:

    def __init__(self):
        self.cache = StyleCache('inventory_api/src/beer_styles.csv')
        self.brew_db = BreweryDBQueries()

    def get_style(self, beer_name):
        beer_name = beer_name.title()
        if self.cache.look_up(beer_name) is not None:
            return self.cache.cache_dict[beer_name]
        try:
            style = self.brew_db.get_beer_style(beer_name)
            self.cache.add(beer_name, style)
            return style
        # pylint: disable=broad-except
        except Exception:
            return 'Unknown'
