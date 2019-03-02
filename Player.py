class Player:

    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.position = 0
        self.properties = []

    def move_forward(self, amount):
        self.position += amount

    def move_backward(self, amount):
        self.position -= amount

    def addMoney(self,amount):
        self.money += amount

    def subtractMoney(self,amount):
        self.money -= amount

    def getProperties(self, number):
        self.properties = number
        return self.properties
