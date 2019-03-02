import Monopoly
import Player
import random

player1 = Player("person1", 1000, 0, [])
player2 = Player("person2", 1000, 0, [])
players = [player1, player2]

monopoly = Monopoly(players)
turn = 0

while not monopoly.getGameOver():
    monopoly.do_turn()


        

def get_dice_roll():
    return random.randint(1, 7)

