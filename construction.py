import building
import room


def main():
    print("_________________________________________")
    print("HOME Building")
    living_room_size = float(input("Please enter size of your living room: "))
    kitchen_size = float(input("Please enter size of your kitchen: "))
    dining_size = float(input("Please enter size of your dining room: "))
    number_bed_rooms = int(input("Please enter the number of bedrooms: "))

    """Set items for the Room Object"""
    my_rooms = {}
    for i in range(number_bed_rooms):
        my_bedroom = float(input("Please enter size of bedroom {}: ".format(i + 1)))
        my_rooms.update({"Bedroom{}".format(i + 1): my_bedroom})
    my_rooms.update({"Living Room": living_room_size, "Kitchen": kitchen_size, "Dinning Room": dining_size})

    # the_gas = input("Please enter in 'yes' or 'no' if your house has gas: ").lower()
    # the_water = input("Please enter 'yes' or 'no' if you house has water: ").lower()
    rooms_1 = room.Room()
    rooms_1.set_square_feet(my_rooms)
    # rooms_1.set_gas(the_gas)
    # rooms_1.set_water(the_water)

    """Drop rooms attribute into House Object"""
    house = building.House(rooms_1.get_square_feet())
    """Call the function for Polymorphism and print"""
    print("\nHOME")
    print("____________________")
    print("Your Home Siding is: {}".format(house.get_siding()))
    get_total_square_feet(house)

    # Commercial Building
    """Set items for the Room Object"""
    print("_________________________________________")
    print("COMMERCIAL Building")
    number_rooms = int(input("Please enter the number of rooms in your commercial building: "))
    my_com_rooms = {}
    for i in range(number_rooms):
        my_room = float(input("Please enter size of room {}: ".format(i + 1)))
        my_com_rooms.update({"room{}".format(i + 1): my_room})

    rooms_2 = room.Room()
    rooms_2.set_square_feet(my_com_rooms)

    print("\nCOMMERCIAL BUILDING")
    print("____________________")
    com_building = building.Commercial(rooms_2.get_square_feet())
    print("Your Commercial Building Siding is: {}".format(com_building.get_siding()))
    # Call the Polymorphism function
    get_total_square_feet(com_building)


# Polymorphism
def get_total_square_feet(sft):
    sft.total_square_feet()


if __name__ == '__main__':
    main()


