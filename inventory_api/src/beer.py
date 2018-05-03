class Beer:

    # pylint: disable=too-many-arguments
    def __init__(self, name, size, style, quantity, price):
        self.name = name
        self.size = size
        self.style = style
        self.price = price
        self.quantity = quantity

    def is_available(self):
        if float(self.quantity) > 0.0:
            return True
        return False
