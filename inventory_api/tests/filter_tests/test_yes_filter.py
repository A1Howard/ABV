from inventory_api.filters.yes_filter import YesFilter


def test_is_match_is_true():
    assert YesFilter().is_match(None) is True
