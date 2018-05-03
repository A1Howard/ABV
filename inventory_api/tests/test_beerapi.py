from inventory_api.tests.mock_inventory_queries import MockInventoryQueries
from inventory_api.tests.mock_inventory_queries_saving import MockInventoryQueriesSaving
from beer import Beer
from data_collector.src.file_location import FileLocation
import beerapi


beerapi.APP.testing = True
APP = beerapi.APP.test_client()
PABST = Beer(name='Pabst', size='12/12oz', style='lager', quantity='1', price='20')
GUINNESS = Beer(name='Guinness', size='12/12oz', style='stout', quantity='1', price='30')


def test_empty_results():
    beerapi.QUERIES = MockInventoryQueries([])
    result = APP.get('/current')
    assert result.data == b'[]'


def test_single_result():
    beerapi.QUERIES = MockInventoryQueries([PABST])
    result = APP.get('/current')
    assert eval(result.data)[0]['name'] == 'Pabst'


def test_two_results():
    beerapi.QUERIES = MockInventoryQueries([PABST, GUINNESS])
    result = APP.get('/current')
    assert eval(result.data)[0]['name'] == 'Pabst'
    assert eval(result.data)[1]['name'] == 'Guinness'


def test_no_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.QUERIES = saver
    APP.get('/current')
    assert saver.filter.name is None
    assert saver.filter.style is None


def test_name_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.QUERIES = saver
    APP.get('/current?name=Guinness')
    assert beerapi.QUERIES.filter.name == 'Guinness'
    assert saver.filter.style is None


def test_availability_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.QUERIES = saver
    APP.get('/current?name=Guinness&availability=2')
    assert saver.filter.name == 'Guinness'
    assert saver.filter.availability == '2'
    assert saver.filter.style is None


def test_style_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.QUERIES = saver
    APP.get('/current?name=Guinness&availability=2&style=stout')
    assert saver.filter.name == 'Guinness'
    assert saver.filter.availability == '2'
    assert saver.filter.style == 'stout'
    assert saver.filter.size is None


def test_size_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.QUERIES = saver
    APP.get('/current?name=Guinness&availability=2&style=stout&size=12/12OZ')
    assert saver.filter.name == 'Guinness'
    assert saver.filter.availability == '2'
    assert saver.filter.style == 'stout'
    assert saver.filter.size == '12/12OZ'


def test_repeat_params():
    saver = MockInventoryQueriesSaving()
    beerapi.QUERIES = saver
    APP.get('/current?name=Guinness&name=Pabst')
    assert saver.filter.name == 'Guinness'


def test_bad_params():
    saver = MockInventoryQueriesSaving()
    beerapi.QUERIES = saver
    result = APP.get('/current?foo=bar')
    assert result.status_code == 400


def test_bad_and_good_params():
    saver = MockInventoryQueriesSaving()
    beerapi.QUERIES = saver
    result = APP.get('/current?name=Guinness&foo=bar')
    assert result.status_code == 400


def test_api_initialization():
    FileLocation.save_location = 'inventory_api/tests/sample_csv_files'
    beerapi.initialize_inventory()
    assert beerapi.QUERIES.inventory.get_historic_inventory()[0].name == 'BREW WORKS HOP EXPLOSION'
