# pylint: disable=missing-docstring
class StyleFilter:

    # pylint: disable=too-few-public-methods
    def __init__(self, subfilter, style):
        self.subfilter = subfilter
        self.style = style

    def is_match(self, beer):
        if self.style not in beer.style:
            return False
        return self.subfilter.is_match(beer)
