import pytest
import requests
import requests_mock
import re
from abv.inventory_api.brewerydb_queries import BreweryDBQueries


def verify(the_json, beer_name, expected):
    with requests_mock.Mocker() as session:
        BREWERYDB_URI = re.compile('api.brewerydb.com')
        session.register_uri('GET', BREWERYDB_URI, json=the_json)

        b = BreweryDBQueries()

        style = b.get_beer_style(beer_name)
        assert style == expected


def test_no_data_available():
    the_json = {'status': 'success'}
    beer_name = 'Guinness'
    expected = 'Unknown'
    verify(the_json, beer_name, expected)


def test_no_style_available():
    the_json = {'status': 'success', 'data': [{}]}
    beer_name = 'Guinness'
    expected = 'Unknown'
    verify(the_json, beer_name, expected)


def test_no_name_of_style_available():
    the_json = {'status': 'success', 'data': [{'style': {'name': '', 'shortName': ''}}]}
    beer_name = 'Guinness'
    expected = 'Unknown'
    verify(the_json, beer_name, expected)


def test_long_name_available():
    the_json = {'status': 'success', 'data': [{'style': {'name': 'Irish Imperial Stout',
                                                         'shortName': ''}}]}
    beer_name = 'Guinness'
    expected = 'Irish Imperial Stout'
    verify(the_json, beer_name, expected)


def test_short_name_available():
    the_json = {'status': 'success', 'data': [{'style': {'name': 'Irish Imperial Stout',
                                                         'shortName': 'Stout'}}]}
    beer_name = 'Guinness'
    expected = 'Stout'
    verify(the_json, beer_name, expected)