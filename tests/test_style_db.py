from tests.mock_brewery_db import MockBreweryDBStoutTracked
from tests.mock_brewery_db import MockBreweryDBAlwaysError
from tests.mock_brewery_db import MockBreweryDBUnknownTracked
from abv.style_db import StyleDB



#Tests that stout is correctly returned when cache has it. Also that database is never seached
def test_cache_has_beer():
    styles = StyleDB()
    styles.brew_db = MockBreweryDBStoutTracked
    assert styles.get_style('Nitro') == 'stout'
    assert styles.brew_db.count == 0

#Tests if the database has the style and not the cache. And then second search takes from cache.
def test_db_has_style_and_then_cache():
    styles = StyleDB()
    styles.brew_db = MockBreweryDBStoutTracked
    tested = styles.get_style('Guinness')
    print(tested)
    assert styles.get_style('Guinness') == 'stout'
    assert styles.get_style('Guinness') == 'stout'
    assert styles.brew_db.count == 1

#Tests if unknown is first found by database and then from cache
def test_unknown_from_db_then_cache():
    styles = StyleDB()
    styles.beer_dict = MockBreweryDBUnknownTracked
    assert styles.get_style('Duck Tails') == 'Unknown'
    assert styles.get_style('Duck Tails') == 'Unknown'
    assert styles.brew_db.count == 1

#Tests that if query throws error once, that it throws it again by same input
def test_two_against_db():
    styles = StyleDB()
    styles.brew_db = MockBreweryDBAlwaysError
    assert styles.get_style('Guinness') == "Unknown"
    assert styles.get_style('Guinness') == "Unknown"
    assert styles.brew_db.count == 2
