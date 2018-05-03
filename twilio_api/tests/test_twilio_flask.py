# pylint: disable=redefined-outer-name
import re
from pytest import fixture
import requests_mock
import twilio_flask


@fixture()
def app():
    twilio_flask.APP.testing = True
    inner_app = twilio_flask.APP.test_client()
    return inner_app


def test_bad_status_code(app):
    with requests_mock.Mocker() as m:
        m.register_uri('GET', re.compile('0.0.0.0:10000'), text='[]', status_code=404)
        result = app.get('/', data={'Body':'stout'})
        assert b'Sorry, I cannot handle your request. Please try again later!' in result.data


def test_valid_twilio_format(app):
    with requests_mock.Mocker() as m:
        m.register_uri('GET', re.compile('0.0.0.0:10000'), text='[{"name":"foo"}, {"name":"foo"}]')
        result = app.get('/', data={'Body': 'stout'})
        assert result.status_code == 200
        assert result.data.startswith(b'<?xml')


def test_no_results(app):
    with requests_mock.Mocker() as m:
        m.register_uri('GET', re.compile('0.0.0.0:10000'), text='[]')
        style = 'stout'
        result = app.get('/', data={'Body': style})
        expected = 'Sorry, no results for {}'.format(style)
        assert bytes(expected, 'utf-8') in result.data


def test_one_result(app):
    with requests_mock.Mocker() as m:
        m.register_uri('GET', re.compile('0.0.0.0:10000'), text='[{"name":"foo"}]')
        result = app.get('/', data={'Body': 'porter'})
        assert b'There is 1 beer with the style porter' in result.data


def test_tw0_result(app):
    with requests_mock.Mocker() as m:
        m.register_uri('GET', re.compile('0.0.0.0:10000'), text='[{"name":"foo"}, {"name":"bar"}]')
        result = app.get('/', data={'Body': 'IPA'})
        assert b'There are 2 beers with the style IPA' in result.data


def test_count_beers():
    query_results = ['{}', '{}']
    assert len(query_results) == 2
    assert twilio_flask.get_num_matching_beers(query_results)