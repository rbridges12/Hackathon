class Chance:
    def __init__(self, myspaces, myprice, myname):
        self.spaces = myspaces
        self.price = myprice
        self.name = myname

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_spaces(self):
        return self.spaces