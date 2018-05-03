from inventory_api.filters.size_filter import SizeFilter
from inventory_api.src.beer import Beer
from inventory_api.filters.yes_filter import YesFilter


def test_size_filter_match():
    b = Beer('bud', '1/2 keg', 'lager', '2.00', '1.00')
    f = SizeFilter(YesFilter(), '1/2 keg')
    assert f.is_match(b) is True


def test_size_filter_no_match():
    b = Beer('bud', '1/2 keg', 'lager', '2.00', '1.00')
    f = SizeFilter(YesFilter(), 'pint')
    assert f.is_match(b) is False
