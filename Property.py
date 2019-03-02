class Property:
    def __init__(self, myname, myprice, mycolor, myrent, myhouses, myhotel, mylocation):
        self.name = myname
        self.price = myprice
        self.color = mycolor
        self.rent = myrent
        self.houses = myhouses
        self.hotel = myhotel
        self.owner = 0
        self.location = mylocation

    def buy(self, player):
        self.owner = player

    def buy_house(self, numhouse):
        if (self.houses + numhouse) < 5:
            self.houses = self.houses + numhouse
        else:
            self.houses = 0
            self.hotel = 1

    def get_owner(self):
        return self.owner

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_price(self):
        return self.price

    def set_owner(self, player):
        self.owner = player

    def get_rent(self):
        return self.rent





