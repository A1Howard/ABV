class MockInventoryQueriesSaving():

    def __init__(self):
        pass

    def get_filtered_inventory(self, filter):
        self.filter = filter
        return []
