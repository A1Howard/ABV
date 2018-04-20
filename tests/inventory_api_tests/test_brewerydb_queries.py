import pytest
import requests
import requests_mock
import re
from abv.inventory_api.brewerydb_queries import BreweryDBQueries


def verify(the_json, beer_name, request_count, expected):
    with requests_mock.Mocker() as session:
        brewery_uri = re.compile('api.brewerydb.com')
        session.register_uri('GET', brewery_uri, json=the_json)
        b = BreweryDBQueries()

        b.num_queries_today = request_count
        style = b.get_beer_style(beer_name)
        assert style == expected


def test_no_data_available():
    the_json = {'status': 'success'}
    beer_name = 'Guinness'
    request_count = 10
    expected = 'Unknown'
    verify(the_json, beer_name, request_count, expected)


def test_no_style_available():
    the_json = {'status': 'success', 'data': [{}]}
    beer_name = 'Guinness'
    request_count = 10
    expected = 'Unknown'
    verify(the_json, beer_name, request_count, expected)


def test_no_name_of_style_available():
    the_json = {'status': 'success', 'data': [{'style': {'name': '', 'shortName': ''}}]}
    beer_name = 'Guinness'
    request_count = 10
    expected = 'Unknown'
    verify(the_json, beer_name, request_count, expected)


def test_long_name_available():
    the_json = {'status': 'success', 'data': [{'style': {'name': 'Irish Imperial Stout',
                                                         'shortName': ''}}]}
    beer_name = 'Guinness'
    request_count = 10
    expected = 'Irish Imperial Stout'
    verify(the_json, beer_name, request_count, expected)


def test_short_name_available():
    the_json = {'status': 'success', 'data': [{'style': {'name': 'Irish Imperial Stout',
                                                         'shortName': 'Stout'}}]}
    beer_name = 'Guinness'
    request_count = 10
    expected = 'Stout'
    verify(the_json, beer_name, request_count, expected)


def test_requests_limit_too_high():
    the_json = {'status': 'success', 'data': [{'style': {'name': 'Irish Imperial Stout',
                                                         'shortName': 'Stout'}}]}
    beer_name = 'Guinness'
    request_count = 390
    expected = ''
    verify(the_json, beer_name, request_count, expected)


def test_requests_limit_good():
    the_json = {'status': 'success', 'data': [{'style': {'name': 'Irish Imperial Stout',
                                                         'shortName': 'Stout'}}]}
    beer_name = 'Guinness'
    request_count = 389
    expected = 'Stout'
    verify(the_json, beer_name, request_count, expected)


@pytest.fixture(params=[requests.RequestException])
def failed_request(request):
    with requests_mock.Mocker() as session:
        brewery_uri = re.compile('api.brewerydb.com')
        session.register_uri('GET', brewery_uri, exc=request.param)
        yield request.param


def test_failed_request(failed_request):
    b = BreweryDBQueries()
    style = b.get_beer_style('Guinness')
    assert style == ''
