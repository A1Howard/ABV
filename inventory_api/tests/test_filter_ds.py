from filter_ds import FilterDS


def test_filter_with_no_filters():
    ds_filter = FilterDS()
    assert ds_filter.size is None
    assert ds_filter.style is None


def test_filter_with_package_filter():
    ds_filter = FilterDS(size='keg')
    assert ds_filter.size == 'keg'
    assert ds_filter.style is None


def test_filter_with_style_filter():
    ds_filter = FilterDS(style='porter')
    assert ds_filter.size is None
    assert ds_filter.style == 'porter'


def test_filter_with_both_filters():
    ds_filter = FilterDS(size='keg', style='porter')
    assert ds_filter.size == 'keg'
    assert ds_filter.style == 'porter'
