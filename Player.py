import Property

class Player:

    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.position = 1
        self.properties = []

    def move_forward(self, amount):
        self.position += amount
        if self.position >= 40:
            self.position = 1
            print(self.name, " passed go, earned $200")
            self.add_money(200)

    def move_backward(self, amount):
        self.position -= amount

    def add_money(self,amount):
        self.money += amount

    def subtract_money(self,amount):
        self.money -= amount

    def get_properties(self):
        return self.properties

    def get_position(self):
        return self.position

    def get_money(self):
        return self.money

    def get_name(self):
        return self.name


