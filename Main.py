import Monopoly
import Player
import matplotlib.pyplot

player1 = Player.Player("person1")
player2 = Player.Player("person2")
player3 = Player.Player("Person3")
player4 = Player.Player("Person4")
players = [player1, player2, player3, player4]

monopoly = Monopoly.Monopoly(players)
turn = 0
time = []
player1_money = []
player1_position = [0]*40
player2_money = [40]
player2_position = []
player3_money = []
player4_money = []


def get_data():
    time.append(turn)
    player1_money.append(monopoly.get_players()[0].get_money())
    player2_money.append(monopoly.get_players()[1].get_money())
    player3_money.append(monopoly.get_players()[2].get_money())
    player4_money.append(monopoly.get_players()[3].get_money())
    #player1_position.append(monopoly.get_players()[0].get_position())
    #player2_position.append(monopoly.get_players()[1].get_position())
    player1_position[monopoly.get_players()[0].get_position()] += 1


def graph_money_data():
    matplotlib.pyplot.ylabel("Money")
    matplotlib.pyplot.xlabel("Turn")
    matplotlib.pyplot.plot(time, player1_money, "b-")
    matplotlib.pyplot.plot(time, player2_money, "r-")
    matplotlib.pyplot.plot(time, player3_money, "g-")
    matplotlib.pyplot.plot(time, player4_money, "m-")
    matplotlib.pyplot.legend(("player 1", "player 2", "player 3", "player 4"), loc='lower right')
    matplotlib.pyplot.show()


def graph_position_data():
    print(player1_position)
    print(turn)
    matplotlib.pyplot.ylabel("Times Landed On")
    matplotlib.pyplot.xlabel("Square")
    matplotlib.pyplot.plot(range(40), player1_position)
    matplotlib.pyplot.show()


while not monopoly.get_game_over():
    monopoly.do_turn()
    get_data()
    turn += 1

for i in players:
    print(i.get_name(), "Won!")
for i in monopoly.get_properties():
    print(i.get_owner())
    if not i.get_owner() is None:
        print(i.get_name())


graph_position_data()

