class SizeFilter:

    def __init__(self, subfilter, size):
        self.subfilter = subfilter
        self.size = size

    def is_match(self, beer):
        if self.size not in beer.size:
            return False
        return self.subfilter.is_match(beer)
