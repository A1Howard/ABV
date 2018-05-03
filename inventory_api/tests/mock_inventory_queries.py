# pylint: disable=unused-argument
class MockInventoryQueries:

    def __init__(self, results):
        self.results = results

    def get_filtered_inventory(self, beer_ds):
        return self.results
