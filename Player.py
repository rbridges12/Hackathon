class Player:


    def __init__(self, money, position, properties):
        self.money = money
        self.position = position
        self.properties = properties
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