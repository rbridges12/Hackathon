import Property.py


class Monopoly:
    def __init__(self, players):
        self.players = players

    def __create_properties(self):
        self.properties = []
        self.properties.append(Property.Property("Test Property", 500, "blue", 15, 0, 0))
    def __create_chance(self):
        self.chance = []
        self.chance.append(Chance.Chance(0,50,"Win a beauty contest. Collect $50"))
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
