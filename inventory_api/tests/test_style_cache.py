import tempfile
from style_cache import StyleCache


def test_blank_file():
    test_cache = StyleCache("beer_data/empty.csv")
    print(test_cache.cache_dict)
    assert test_cache.cache_dict == {}


def test_can_read_and_lookup():
    test_cache = StyleCache("inventory_api/tests/sample_csv_files/beer_and_style.csv")
    assert test_cache.look_up("Guinness") == "Stout"
    assert test_cache.look_up("Pabst Blue Ribbon") == "Lager"
    assert test_cache.look_up("Fat Tire") == "Belgian Ale"


def test_invalid_beer_lookup():
    test_cache = StyleCache("inventory_api/tests/sample_csv_files/beer_and_style.csv")
    assert test_cache.look_up("Rude Elf Reserve") is None


def test_add_beer():
    temp_file = tempfile.NamedTemporaryFile(dir='inventory_api/tests/sample_csv_files', prefix='b')
    test_cache = StyleCache(temp_file.name)
    test_cache.add("Rude Elf Reserve", "Belgian")
    assert test_cache.look_up("Rude Elf Reserve") == "Belgian"
