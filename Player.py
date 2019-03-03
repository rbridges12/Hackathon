
class Player:

    def __init__(self, name, initial_money=1500, initial_position=0, initial_properties=[], num_of_squares=40):
        self.__name = name
        self.__money = initial_money
        self.__position = initial_position
        self.__properties = initial_properties
        self.__num_of_squares = num_of_squares
        self.__is_bankrupt = False

    def move_forward(self, amount):
        self.__position += amount
        if self.__position >= 40:
            self.__position %= 40
            print(self.__name, " passed go, earned $200")
            self.add_money(200)

    def increment_position(self):
        self.__position += 1
        if self.__position > 40:
            self.__position = 1;

    def add_money(self,amount):
        self.__money += amount

    def subtract_money(self,amount):
        self.__money -= amount

    def set_name(self, name):
        self.__name = name

    def set_money(self, money):
        if money < 0:
            raise ValueError("Player cannot have negative money")
        self.__money = money

    def set_position(self, position):
        if position > 40 or position < 0:
            raise ValueError("Position must be an integer between 1 and 40")
        self.__position = abs(position % self.__num_of_squares)

    def set_properties(self, properties):
        self.__properties = properties

    def set_num_of_squares(self, num_of_squares):
        self.__num_of_squares = num_of_squares

    def set_is_bankrupt(self, is_bankrupt):
            self.__is_bankrupt = is_bankrupt

    def get_name(self):
        return self.__name

    def get_money(self):
        return self.__money

    def get_position(self):
        return self.__position

    def get_properties(self):
        return self.__properties

    def get_num_of_squares(self):
        return self.__num_of_squares

    def get_is_bankrupt(self):
        return self.__is_bankrupt



