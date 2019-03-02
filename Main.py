import Monopoly.py
import Player.py
import random

player1 = Player("person1", 1000, 0, [])
player2 = Player("person2", 1000, 0, [])
players = [player1, player2]

monopoly = Monopoly(players)
turn = 0

while not monopoly.getGameOver():


def do_turn():
    for player in monopoly.getPlayers():
        player.move_forward(get_dice_roll())
        player_position = player.get_position()
        

def get_dice_roll():
    return random.randint(1,7)

def landed_on_property():

def landed_on_chance():
