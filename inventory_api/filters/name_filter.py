class NameFilter:

    def __init__(self, subfilter, name):
        self.subfilter = subfilter
        self.name = name

    def is_match(self, beer):
        if self.name not in beer.name:
            return False
        return self.subfilter.is_match(beer)
