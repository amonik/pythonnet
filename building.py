class Building:
    def __init__(self, siding):
        self.__siding = siding

    def set_siding(self, siding):
        self.__siding = siding

    def get_siding(self):
        return self.__siding

    def __str__(self):
        return self.__siding


# Inheritance of Building
class House(Building):
    def __init__(self, rooms):
        Building.__init__(self, "Brick")
        self.__rooms = rooms
        self.__total = 0

    def set_rooms(self, rooms):
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms

    def total_square_feet(self):
        for k, v in self.__rooms.items():
            self.__total += v
        print("The total square feet of your Home is: {} square feet.\n"
              .format(self.__total))


# Inheritance of Building
class Commercial(Building):
    def __init__(self, rooms):
        Building.__init__(self, 'Stone')
        self.__rooms = rooms
        self.__total = 0

    def set_rooms(self, rooms):
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms

    def total_square_feet(self):
        for k, v in self.__rooms.items():
            self.__total += v
        print("The total square feet of your Commercial building is: {} square feet.\n"
              .format(self.__total))
