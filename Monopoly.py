import Property.py


class Monopoly:
    def __init__(self, players):
        self.players = players

    def __create_properties(self):
        self.properties = []
        self.properties.append(Property.Property("Test Property", 500, "blue", 15, 0, 0))