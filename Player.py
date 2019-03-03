
class Player:

    def __init__(self, name, initial_money=1500, initial_position=0, initial_properties=[], num_of_squares=40):
        self.name = name
        self.money = initial_money
        self.position = initial_position
        self.properties = initial_properties
        self.num_of_squares = num_of_squares
        self.is_bankrupt = False

    def move_forward(self, amount):
        self.position += amount
        if self.position >= 40:
            self.position = 1
            print(self.name, " passed go, earned $200")
            self.add_money(200)

    def increment_position(self):
        self.position += 1
        if self.position > 40:
            position = 1;

    def add_money(self,amount):
        self.money += amount

    def subtract_money(self,amount):
        self.money -= amount

    def set_name(self, name):
        self.name = name

    def set_money(self, money):
        if money < 0:
            raise ValueError("Player cannot have negative money")
        self.money = money

    def set_position(self, position):
        if position > 40 or position < 0:
            raise ValueError("Position must be an integer between 1 and 40")
        self.position = abs(position % self.num_of_squares)

    def set_properties(self, properties):
        self.properties = properties

    def set_num_of_squares(self, num_of_squares):
        self.num_of_squares = num_of_squares

    def set_is_bankrupt(self, is_bankrupt):
            self.is_bankrupt = is_bankrupt

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def get_position(self):
        return self.position

    def get_properties(self):
        return self.properties

    def get_num_of_squares(self):
        return self.num_of_squares

    def get_is_bankrupt(self):
        return self.is_bankrupt



