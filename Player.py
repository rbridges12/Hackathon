
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
            self.position %= 40
            print(self.name, " passed go, earned $200")
            self.add_money(200)

    def increment_position(self):
        self.position += 1
        if self.position > 40:
            self.position = 1;

    def set_position(self, position):
        if position > 40 or position < 0:
            raise ValueError("Position must be an integer between 1 and 40")
        self.position = abs(position % self.num_of_squares)
