class Room:
    def __init__(self):
        self.__square_feet = {}
        self.__water = False
        self.__gas = False

    def set_square_feet(self, square_feet):
        self.__square_feet = square_feet

    def set_water(self, water):
        if water == 'yes':
            water = True
        else:
            water = False
        self.__water = water

    def set_gas(self, gas):
        if gas == 'yes':
            gas = True
        else:
            gas = False
        self.__gas = gas

    def get_square_feet(self):
        return self.__square_feet

    def get_water(self):
        if self.__water:
            self.__water = "You have water"
        else:
            self.__water = "You have NO water"
        return self.__water

    def get_gas(self):
        if self.__gas:
            self.__gas = "You have gas"
        else:
            self.__gas = "You have NO gas"
        return self.__gas


