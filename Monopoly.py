import Property
import Chance
import communitychest
import Jail


class Monopoly:
    def __init__(self, players):
        self.players = players
        self.__create_properties()
        self.__create_chance()
        self.__create_communitychest()

    def __create_properties(self):
        self.properties = []
        self.properties.append(Property.Property("Iowa City Lane", 500, "blue", 30, 0, 39))
        self.properties.append(Property.Property("North Liberty Road", 450, "blue", 30, 0, 37))
        self.properties.append(Property.Property("Coralville Court", 400, "green", 25, 0, 34))
        self.properties.append(Property.Property("Cedar Rapids Boulevard", 380, "green", 25, 0, 32))
        self.properties.append(Property.Property("Bettendorf Drive", 360, "green", 25, 0, 31))
        self.properties.append(Property.Property("Misquaki Circle", 320, "yellow", 20, 0, 29))
        self.properties.append(Property.Property("Decorah Highway 6", 300, "yellow", 20, 0, 27))
        self.properties.append(Property.Property("Des Moines Avenue", 280, "yellow", 20, 0, 26))
        self.properties.append(Property.Property("Waterloo Street", 275, "red", 15, 0, 24))
        self.properties.append(Property.Property("Dubuque Freeway", 260, "red", 15, 0, 23))
        self.properties.append(Property.Property("Cedar Falls Drive", 250, "red", 15, 0, 21))
        self.properties.append(Property.Property("Sioux City Circle", 240, "orange", 10, 0, 19))
        self.properties.append(Property.Property("Davenport Avenue", 220, "orange", 10, 0, 18))
        self.properties.append(Property.Property("Ames Avenue", 200, "orange", 10, 0, 16))
        self.properties.append(Property.Property("Council Bluffs Road", 180, "cyan", 7, 0, 14))
        self.properties.append(Property.Property("Pella Parkway", 160, "cyan", 7, 0, 13))
        self.properties.append(Property.Property("Postville Court", 150, "cyan", 7, 0, 11))
        self.properties.append(Property.Property("Storm Lake Circle", 125, "purple", 5, 0, 9))
        self.properties.append(Property.Property("Okoboji Place", 100, "purple", 5, 0, 8))
        self.properties.append(Property.Property("Mason City Boulevard", 90, "purple", 5, 0, 6))
        self.properties.append(Property.Property("Benton Drive", 75, "brown", 2, 0, 3))
        self.properties.append(Property.Property("Riverside Street", 50, "brown", 2, 0, 1))
        self.properties.append(Property.Property("MidAmerican Energy", 150, "white", 50, 0, 12))
        self.properties.append(Property.Property("Mediacom", 150, "white", 50, 0, 28))
        self.properties.append(Property.Property("Will's Treyways", 200, "black", 50, 0, 35))
        self.properties.append(Property.Property("Ray Railways", 200, "black", 50, 0, 25))
        self.properties.append(Property.Property("Bridge's Bridgeway", 200, "black", 50, 0, 15))
        self.properties.append(Property.Property("Gavel's Gravel", 200, "black", 50, 0, 5))

    def __create_chance(self,location):
        self.chance = []
        self.chance.append(Chance.Chance(0, 50, "Win a beauty contest. Collect $50"))
        self.chance.append(Chance.Chance(-2, 0, "Slip and fall. Go back 2 spaces"))
        self.chance.append(Chance.Chance(0,-20,"Get a speeding ticket. Pay $20"))
        self.chance.append(Chance.Chance(0,-10,"Lose a bet with the bank. Pay $10"))
        self.chance.append(Chance.Chance(2,0,"Catch a free cab ride. Go forward 2 spaces"))
        self.chance.append(Chance.Chance(0,-100,"Get audited by the IRS. Pay $100"))
        self.chance.append(Chance.Chance(0,-40,"Pay Mr. Monopoly $40 for a new top hat"))
        self.chance.append(Chance.Chance(-3,0,"Get caught up talking to a friend. Go back 3 spaces"))
        self.chance.append(Chance.Chance(0,10,"Bank error in your favor. Collect $10"))
        self.chance.append(Chance.Chance(1,0,"Get a new, faster car. Go forward 1 space"))
        self.chance.append(Chance.Chance(-2,0,"Wake up late. Go back 2 spaces"))
        self.chance.append(Chance.Chance(0,15,"Win a bet with Mr. Monopoly. Collect $15"))
    def __create_communitychest(self):
        self.communitychest = []
        self.communitchest.append(communitychest())

    def get_properties(self):
        return self.properties

    def get_game_over(self):
        not_bankrupt = 0
        for player in self.players:
            if player.getMoney() >= 0:
                not_bankrupt += 1
        if not_bankrupt <= 1:
            return False



