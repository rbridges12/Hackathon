class Property:
    def __init__(self, name, price, rent, color, position, houses=0, owner=None):
        self.__name = name
        self.__price = price
        self.__rent = rent
        self.__color = color
        self.__position = position
        self.__houses = houses
        self.__owner = owner

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_rent(self, rent):
        self.__rent = rent

    def set_color(self, color):
        self.__color = color

    def set_position(self, position):
        self.__position = position

    def set_houses(self, houses):
        self.__houses = houses

    def set_owner(self, owner):
        self.__owner = owner

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_rent(self):
        return self.__rent

    def get_color(self):
        return self.__color

    def get_positon(self):
        return self.__position

    def get_houses(self):
        return self.__houses

    def get_owner(self):
        return self.__owner





