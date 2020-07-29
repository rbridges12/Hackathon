from Property import *
from Chance import *
from communitychest import *
import random


class Monopoly:
    def __init__(self, players, custom_properties = False):
        self.players = players
        self.using_custom_properties = custom_properties
        self.num_bankrupt_players = 0
        self.init_properties()
        self.init_chance()
        self.init_communitychest()
        self.init_board()


    def init_properties(self):
        self.custom_properties = [
            Property(name = "Iowa City Lane", price = 500, color = "blue", rent = 30, position = 39),
            Property(name = "North Liberty Road", price = 450, color = "blue", rent = 30, position = 37),

            Property(name = "Coralville Court", price = 400, color = "green", rent = 25, position = 34),
            Property(name = "Cedar Rapids Boulevard", price = 380, color = "green", rent = 25, position = 32),
            Property(name = "Bettendorf Drive", price = 360, color = "green", rent = 25, position = 31),

            Property(name = "Misquaki Circle", price = 320, color = "yellow", rent = 20, position = 29),
            Property(name = "Decorah Highway 6", price = 300, color = "yellow", rent = 20, position = 27),
            Property(name = "Des Moines Avenue", price = 280, color = "yellow", rent = 20, position = 26),

            Property(name = "Waterloo Street", price = 275, color = "red", rent = 15, position = 24),
            Property(name = "Dubuque Freeway", price = 260, color = "red", rent = 15, position = 23),
            Property(name = "Cedar Falls Drive", price = 250, color = "red", rent = 15, position = 21),

            Property(name = "Sioux City Circle", price = 240, color = "orange", rent = 10, position = 19),
            Property(name = "Davenport Avenue", price = 220, color = "orange", rent = 10, position = 18),
            Property(name = "Ames Avenue", price = 200, color = "orange", rent = 10, position = 16),

            Property(name = "Council Bluffs Road", price = 180, color = "cyan", rent = 7, position = 14),
            Property(name = "Pella Parkway", price = 160, color = "cyan", rent = 7, position = 13),
            Property(name = "Postville Court", price = 150, color = "cyan", rent = 7, position = 11),

            Property(name = "Storm Lake Circle", price = 125, color = "purple", rent = 5, position = 9),
            Property(name = "Okoboji Place", price = 100, color = "purple", rent = 5, position = 8),
            Property(name = "Mason City Boulevard", price = 90, color = "purple", rent = 5, position = 6),

            Property(name = "Benton Drive", price = 75, color = "brown", rent = 2, position = 3),
            Property(name = "Riverside Street", price = 50, color = "brown", rent = 2, position = 1),

            Property(name = "MidAmerican Energy", price = 150, color = "white", rent = 50, position = 12),
            Property(name = "Mediacom", price = 150, color = "white", rent = 50, position = 28),

            Property(name = "Will's Treyways", price = 200, color = "black", rent = 50, position = 35),
            Property(name = "Ray Railways", price = 200, color = "black", rent = 50, position = 25),
            Property(name = "Bridge's Bridgeway", price = 200, color = "black", rent = 50, position = 15),
            Property(name = "Gnavel's Gravel", price = 200, color = "black", rent = 50, position = 5)
        ]

        self.original_properties = [
            Property(name = "Mediterranean Avenue", price = 60, rent = 2, color = "purple", position = 1),
            Property(name = "Baltic Avenue", price = 60, rent = 4, color = "purple", position = 3),

            Property(name = "Oriental Avenue", price = 100, rent = 6, color = "light blue", position = 6),
            Property(name = "Vermont Avenue", price = 100, rent = 6, color = "light blue", position = 8),
            Property(name = "Connecticut Avenue", price = 120, rent = 8, color = "light blue", position = 9),

            Property(name = "St. Charles Place", price = 140, rent = 10, color = "pink", position = 11),
            Property(name = "States Avenue", price = 140, rent = 10, color = "pink", position = 13),
            Property(name = "Virginia Avenue", price = 160, rent = 12, color = "pink", position = 14),

            Property(name = "St. James Place", price = 180, rent = 14, color = "orange", position = 16),
            Property(name = "Tennessee Avenue", price = 180, rent = 14, color = "orange", position = 18),
            Property(name = "New York Avenue", price = 200, rent = 16, color = "orange", position = 19),

            Property(name = "Kentucky Avenue", price = 220, rent = 18, color = "red", position = 21),
            Property(name = "Indiana Avenue", price = 220, rent = 18, color = "red", position = 23),
            Property(name = "Illinois Avenue", price = 240, rent = 20, color = "red", position = 24),

            Property(name = "Atlantic Avenue", price = 260, rent = 22, color = "yellow", position = 26),
            Property(name = "Ventnor Avenue", price = 260, rent = 22, color = "yellow", position = 27),
            Property(name = "Marvin Gardens", price = 280, rent = 24, color = "yellow", position = 29),

            Property(name = "Pacific Avenue", price = 300, rent = 26, color = "green", position = 31),
            Property(name = "North Carolina Avenue", price = 300, rent = 26, color = "green", position = 32),
            Property(name = "Pennsylvania Avenue", price = 320, rent = 28, color = "green", position = 34),

            Property(name = "Park Place", price = 350, rent = 35, color = "blue", position = 37),
            Property(name = "Boardwalk", price = 400, rent = 50, color = "blue", position = 39)
        ]

    def init_chance(self):
        self.chance = [
            Chance(0, 50, "Win a beauty contest. Collect $50"),
            Chance(-2, 0, "Slip and fall. Go back 2 spaces"),
            Chance(0,-20,"Get a speeding ticket. Pay $20"),
            Chance(0,-10,"Lose a bet with the bank. Pay $10"),
            Chance(2,0,"Catch a free cab ride. Go forward 2 spaces"),
            Chance(0,-100,"Get audited by the IRS. Pay $100"),
            Chance(0,-40,"Pay Mr. Monopoly $40 for a new top hat"),
            Chance(-3,0,"Get caught up talking to a friend. Go back 3 spaces"),
            Chance(0,10,"Bank error in your favor. Collect $10"),
            Chance(1,0,"Get a new, faster car. Go forward 1 space"),
            Chance(-2,0,"Wake up late. Go back 2 spaces"),
            Chance(0,15,"Win a bet with Mr. Monopoly. Collect $15")
        ]

    def init_communitychest(self):
        self.communitychest = [
            CommunityChest(0,-40,"Pay the Doc $40"),
            CommunityChest(0, 100, "Get $100 in Christmas Gifts"),
            CommunityChest(3,0, "Wake up early, go 3 spaces")
        ]

    def init_board(self):
        self.board = []
        properties = self.custom_properties if self.using_custom_properties else self.original_properties
        for p in properties:
            board[p.position] = p
        for c in self.chance:
            board[c.position] = c
        for cc in self.communitychest:
            board[cc.position] = cc

    def get_game_over(self):
        return self.num_bankrupt_players >= len(self.players) - 1

    def landed_on_property(self, player, a_property):
        print("%s landed on %s" %(player.name, a_property.name))

        # buy property
        if a_property.owner is None:
            if player.money >= a_property.price:
                if input("Do you want to buy %s? (y/n) " % a_property.name).lower() == "y":
                    a_property.owner = player
                    player.money -= a_property.price
                    print(player.name + "%s bought %s" + a_property.name)
            else:
                print("%s can't buy %s" %(player.name, a_property.name))

        # pay rent
        else:
            owner = a_property.owner
            player.money -= a_property.rent
            owner.money += a_property.rent
            print("%s is owned by %s" %(a_property.name, owner.name))
            print("%s paid %s $%d in rent" % (player.name, owner.name, a_property.rent))

    def landed_on_chance(self, player, chance):
        print(player.name, "landed on chance:", chance.get_description())
        player.move_forward(chance.get_spaces_moved())
        player.add_money(chance.get_price_added())

    #def landed_on_communitychest(self):

    @staticmethod
    def get_dice_roll():
        return random.randint(1, 6) + random.randint(1, 6)

    def get_on_property(self, player_position):
        for a_property in self.original_properties:
            if a_property.position == player_position:
                return a_property
        return None

    def get_on_chance(self, player_position):
        chance_positions = [7, 22, 36]
        for i in chance_positions:
            if player_position == i:
                return self.chance[random.randint(0, len(self.chance)-1)]
        return None

    def get_on_communitychest(self, player_position):
        for c in self.communitychest:
            if c.get_position == player_position:
                return c
            else:
                return None

    def do_turn(self):
        for player in self.players:
            if not player.get_is_bankrupt():
                roll = self.get_dice_roll()
                player.move_forward(roll)
                print(player.name, " has $", player.get_money())
                print(player.name, " rolled a ", roll)
                print(player.name, "moved to tile ", player.position)
                landed_property = self.get_on_property(player.position)
                landed_chance = self.get_on_chance(player.position)
                if landed_property is not None:
                    self.landed_on_property(player, landed_property)
                elif landed_chance is not None:
                    self.landed_on_chance(player, landed_chance)
                if player.get_money() <= 0 or player.get_money() > 10000:
                    player.set_is_bankrupt(True)
                    print(player.name, "is bankrupt")

                    # self.players.remove(player)
