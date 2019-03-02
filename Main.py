import Monopoly
import Player

player1 = Player.Player("person1")
player2 = Player.Player("person2")
players = [player1, player2]

monopoly = Monopoly.Monopoly(players)
turn = 0

while not monopoly.get_game_over():
    monopoly.do_turn()
    turn += 1



