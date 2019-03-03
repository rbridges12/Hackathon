import Monopoly
import Player

player1 = Player.Player("person1")
player2 = Player.Player("person2")
player3 = Player.Player("Person3")
player4 = Player.Player("Person4")
players = [player1, player2, player3, player4]

monopoly = Monopoly.Monopoly(players)
turn = 0

while not monopoly.get_game_over():
    monopoly.do_turn()
    turn += 1

for i in players:
    print(i.get_name(), "Won!")
for i in monopoly.get_properties():
    print(i.get_owner())
    if not i.get_owner() is None:
        print(i.get_name())



