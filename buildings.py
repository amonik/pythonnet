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
    """Initialize with constructor, inherit Building, and pass a value to siding"""
    def __init__(self, rooms):
        Building.__init__(self, "Brick")
        self.__rooms = rooms
        self.__total = 0
    """Getters and Setters"""
    def set_rooms(self, rooms):
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms
    """Loop through the dict and add the values to get the total"""
    def total_square_feet(self):
        for k, v in self.__rooms.items():
            print("The size of {} is: {}".format(k, v))
            self.__total += v
        print("The total square feet of your Home is: {} square feet.\n"
              .format(self.__total))


# Inheritance of Building
class Commercial(Building):
    """Initialize with constructor, inherit Building, and pass a value to siding"""
    def __init__(self, rooms):
        Building.__init__(self, 'Stone')
        self.__rooms = rooms
        self.__total = 0
    """Getters and setters"""
    def set_rooms(self, rooms):
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms

    """Loop through the dict and add the values to get the total"""
    def total_square_feet(self):
        for k, v in self.__rooms.items():
            print("The size of {} is: {}".format(k, v))
            self.__total += v
        print("The total square feet of your Commercial building is: {} square feet.\n"
              .format(self.__total))
