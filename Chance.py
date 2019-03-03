class Chance:
    def __init__(self, spaces_moved, price_added, description):
        self.__spaces_moved = spaces_moved
        self.__price_added = price_added
        self.__description = description

    def set_description(self, description):
        self.__description = description

    def set_spaces_moved(self, spaces):
        self.__spaces_moved = spaces

    def set_price_added(self, price):
        self.__price_added = price

    def get_description(self):
        return self.__description

    def get_price_added(self):
        return self.__price_added

    def get_spaces_moved(self):
        return self.__spaces_moved

    def get_type(self):
        return "chance"
