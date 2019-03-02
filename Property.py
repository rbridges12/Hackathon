class Property:
    def __init__(self, myname, myprice, mycolor, myrent, myhouses, myhotel, myowner):
        self.name = myname
        self.price = myprice
        self.color = mycolor
        self.rent = myrent
        self.houses = myhouses
        self.hotel = myhotel
        self.owner = myowner
    def bought(self, player):
        self.owner = player
    def buy_house(self, numhouse):
        if (self.houses + numhouse) < 5:
            self.houses = self.houses + numhouse
        else:
            self.houses = 0
            self.hotel = 1
    








