import Property
import Chance
import communitychest
import random


class Monopoly:
    def __init__(self, players):
        self.players = players
        self.__create_properties()
        self.__create_chance()
        self.__create_communitychest()

    def __create_properties(self):
        # TODO change arguments to match new order
        # TODO update positions to index from 0 instead of 1
        self.custom_properties = [
            Property.Property("Iowa City Lane", 500, "blue", 30, 0, 39),
            Property.Property("North Liberty Road", 450, "blue", 30, 0, 37),
            Property.Property("Coralville Court", 400, "green", 25, 0, 34),
            Property.Property("Cedar Rapids Boulevard", 380, "green", 25, 0, 32),
            Property.Property("Bettendorf Drive", 360, "green", 25, 0, 31),
            Property.Property("Misquaki Circle", 320, "yellow", 20, 0, 29),
            Property.Property("Decorah Highway 6", 300, "yellow", 20, 0, 27),
            Property.Property("Des Moines Avenue", 280, "yellow", 20, 0, 26),
            Property.Property("Waterloo Street", 275, "red", 15, 0, 24),
            Property.Property("Dubuque Freeway", 260, "red", 15, 0, 23),
            Property.Property("Cedar Falls Drive", 250, "red", 15, 0, 21),
            Property.Property("Sioux City Circle", 240, "orange", 10, 0, 19),
            Property.Property("Davenport Avenue", 220, "orange", 10, 0, 18),
            Property.Property("Ames Avenue", 200, "orange", 10, 0, 16),
            Property.Property("Council Bluffs Road", 180, "cyan", 7, 0, 14),
            Property.Property("Pella Parkway", 160, "cyan", 7, 0, 13),
            Property.Property("Postville Court", 150, "cyan", 7, 0, 11),
            Property.Property("Storm Lake Circle", 125, "purple", 5, 0, 9),
            Property.Property("Okoboji Place", 100, "purple", 5, 0, 8),
            Property.Property("Mason City Boulevard", 90, "purple", 5, 0, 6),
            Property.Property("Benton Drive", 75, "brown", 2, 0, 3),
            Property.Property("Riverside Street", 50, "brown", 2, 0, 1),
            Property.Property("MidAmerican Energy", 150, "white", 50, 0, 12),
            Property.Property("Mediacom", 150, "white", 50, 0, 28),
            Property.Property("Will's Treyways", 200, "black", 50, 0, 35),
            Property.Property("Ray Railways", 200, "black", 50, 0, 25),
            Property.Property("Bridge's Bridgeway", 200, "black", 50, 0, 15),
            Property.Property("Gavel's Gravel", 200, "black", 50, 0, 5)
        ]

        self.original_properties = [
            Property.Property("Mediterranean Avenue", 60, 2, "purple", 1),
            Property.Property("Baltic Avenue", 60, 4, "purple", 3),
            Property.Property("Oriental Avenue", 100, 6, "light blue", 6),
            Property.Property("Vermont Avenue", 100, 6, "light blue", 8),
            Property.Property("Connecticut Avenue", 120, 8, "light blue", 9),
            Property.Property("St. Charles Place", 140, 10, "pink", 11),
            Property.Property("States Avenue", 140, 10, "pink", 13),
            Property.Property("Virginia Avenue", 160, 12, "pink", 14),
            Property.Property("St. James Place", 180, 14, "orange", 16),
            Property.Property("Tennessee Avenue", 180, 14, "orange", 18),
            Property.Property("New York Avenue", 200, 16, "orange", 19),
            Property.Property("Kentucky Avenue", 220, 18, "red", 21),
            Property.Property("Indiana Avenue", 220, 18, "red", 23),
            Property.Property("Illinois Avenue", 240, 20, "red", 24),
            Property.Property("Atlantic Avenue", 260, 22, "yellow", 26),
            Property.Property("Ventnor Avenue", 260, 22, "yellow", 27),
            Property.Property("Marvin Gardens", 280, 24, "yellow", 29),
            Property.Property("Pacific Avenue", 300, 26, "green", 31),
            Property.Property("North Carolina Avenue", 300, 26, "green", 32),
            Property.Property("Pennsylvania Avenue", 320, 28, "green", 34),
            Property.Property("Park Place", 350, 35, "blue", 37),
            Property.Property("Boardwalk", 400, 50, "blue", 39)
        ]

    def __create_chance(self):
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
        self.communitychest.append(communitychest.CommunityChest(0,-40,"Pay the Doc $40"))
        self.communitychest.append(communitychest.CommunityChest(0, 100, "Get $100 in Christmas Gifts"))
        self.communitychest.append(communitychest.CommunityChest(3,0, "Wake up early, go 3 spaces"))

    def get_properties(self):
        return self.custom_properties

    def get_players(self):
        return self.players

    def get_game_over(self):
        not_bankrupt = 0
        for player in self.players:
            if player.get_money() >= 0:
                not_bankrupt += 1
        if not_bankrupt <= 1:
            return True

    def landed_on_property(self, player, a_property):
        print(player.get_name(), " landed on ", a_property.get_name())
        if a_property.get_owner() == 0:
            if player.get_money() >= a_property.get_price():
                if input("Do you want to buy " + a_property.get_name() + "? (y/n)") == "y":
                    a_property.set_owner(player)
                    player.subtract_money(a_property.get_price())
                    print(player.get_name() + " bought " + a_property.get_name())
            else:
                print(player.get_name() + " can't buy " + a_property.get_name())
        else:
            owner = a_property.get_owner()
            player.subtract_money(a_property.get_rent())
            owner.add_money(a_property.get_rent())
            print(player.get_name() + " paid " + owner.get_name())

    def landed_on_chance(self, player, chance):
        print(player.get_name(), "landed on chance: ", chance.get_name())
        player.move_forward(chance.get_spaces())
        player.add_money(chance.get_price())

    #def landed_on_communitychest(self):

    def __get_dice_roll(self):
        return random.randint(1, 6)

    def get_on_property(self, player_location):
        for a_property in self.custom_properties:
            if a_property.get_location() == player_location:
                return a_property
        return 0

    def get_on_chance(self, player_location):
        chance_locations = [7, 22, 36]
        for i in chance_locations:
            if player_location == i:
                return self.chance[random.randint(0, len(self.chance)-1)]
        return 0

    def get_on_communitychest(self, player_location):
        for c in self.communitychest:
            if c.get_location == player_location:
                return c
            else:
                return 0

    def do_turn(self):
        for player in self.players:
            roll = self.__get_dice_roll()
            player.move_forward(roll)
            print(player.get_name(), " has $", player.get_money())
            print(player.get_name(), " rolled a ", roll)
            landed_property = self.get_on_property(player.get_position())
            landed_chance = self.get_on_chance(player.get_position())
            if landed_property != 0:
                self.landed_on_property(player, landed_property)
            elif landed_chance != 0:
                self.landed_on_chance(player, landed_chance)







