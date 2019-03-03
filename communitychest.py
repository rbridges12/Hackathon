class CommunityChest:
    def __init__(self,myspaces,myprice,myname):
        self.__spaces_moved = myspaces
        self.__price = myprice
        self.__name = myname
    def get_price(self):
        return self.__price
    def get_spaces_moved(self):
        return self.__sapces_moved
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def set_spaces_moved(self,spaces_moved):
        self.__spaces_moved = spaces_moved
    def set_price(self,price):
        self.__price = price
    def get_type(self):
        return "Community Chest"


