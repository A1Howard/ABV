import os
import logging
import requests


class BreweryDBQueries:
    def __init__(self):
        self.num_queries_today = 0
        # self.last_query_timestamp
        try:
            if os.environ['BREWERYDB_API_KEY'] is not None:
                self.key = os.environ['BREWERYDB_API_KEY']
            else:
                raise KeyError

        except KeyError:
            self.key = ''

    def get_beer_style(self, beer_name):
        try:
            if self.num_queries_today >= 390:
                raise Exception

            request = requests.get('http://api.brewerydb.com/v2/search?key=' + self.key +
                                   '&q=' + beer_name + '&type=beer')
            logging.info('The request was fetched successfully!')
            if is_unknown(request.json()):
                return 'Unknown'
            return style_name(request.json())

        except requests.RequestException as e:
            error_subclass = type(e).__name__
            logging.exception('The request could not be found: {}'.format(error_subclass))
            return ""


def is_unknown(beer_json):
    if 'data' not in beer_json:
        return True
    if 'style' not in beer_json['data'][0]:
        return True
    beer_name = beer_json['data'][0]['style']['name']
    if len(beer_name) == 0:
        return True
    return False


def style_name(beer_json):
    if 'shortName' not in beer_json['data'][0]['style']:
        return beer_json['data'][0]['style']['name']
    short_name = beer_json['data'][0]['style']['shortName']
    if len(short_name) == 0:
        return beer_json['data'][0]['style']['name']
    return beer_json['data'][0]['style']['shortName']
