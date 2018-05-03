# pylint: disable=too-few-public-methods
class FileLocation:
    """
    This class is contains a static variable holding the location where data is saved.
    The initializer asserts False to ensure the class is never instantiated.
    """

    def __init__(self):
        assert False

    save_location = '/beer_data'
