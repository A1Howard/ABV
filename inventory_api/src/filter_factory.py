from inventory_api.filters.size_filter import SizeFilter
from inventory_api.filters.name_filter import NameFilter
from inventory_api.filters.yes_filter import YesFilter
from inventory_api.filters.style_filter import StyleFilter
from inventory_api.filters.availability_filter import AvailabilityFilter


def build(filter_ds):
    recursive_filter = YesFilter()
    if filter_ds.size is not None:
        recursive_filter = SizeFilter(recursive_filter, filter_ds.size)
    if filter_ds.name is not None:
        recursive_filter = NameFilter(recursive_filter, filter_ds.name)
    if filter_ds.style is not None:
        recursive_filter = StyleFilter(recursive_filter, filter_ds.style)
    if filter_ds.availability is not None:
        recursive_filter = AvailabilityFilter(recursive_filter, filter_ds.availability)
    return recursive_filter
