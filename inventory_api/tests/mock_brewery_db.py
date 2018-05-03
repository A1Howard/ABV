# pylint: disable=unused-argument
class MockDB:
    count = 0

    def get_beer_style(self, beer_name):
        self.count += 1
        if beer_name == 'Guinness':
            return 'stout'
        elif beer_name == 'Nitro':
            return 'stout'
        elif beer_name == 'Duck Tails':
            return 'Unknown'
        raise Exception('Error')


class MockBreweryDBUnknownTracked:
    count = 0

    def get_style(self, beer_name):
        self.count += 1
        return 'Unknown'


class MockBreweryDBStoutTracked:
    count = 0

    def get_style(self, beer_name):
        self.count += 1
        return 'stout'


class MockBreweryDBAlwaysError:
    count = 0

    def get_style(self, beer_name):
        self.count += 1
        raise Exception('Error')
