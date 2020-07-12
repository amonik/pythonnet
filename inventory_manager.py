import inventory
import pickle
import sys

# Global constants for menu choices
ADD_ITEM = 1
DISPLAY_RECEIPT = 2
SAVE_DISPLAY_RECEIPT = 3
QUIT = 0
my_inventory = inventory.Inventory()
NAME = []
QUANTITY = []
PRICE = []


def quit_program():
    print("Exiting program...")
    sys.exit(0)


# Call all functions below from this main.
def main():
    # Initialize a variable for the user's choice.
    choice = 0
    choice = display_menu()
    if choice == ADD_ITEM:
        print("\nAvailable Items")
        print("_______________")
        add_items()
    elif choice == QUIT:
        quit_program()
    my_inventory.subtotal()


# Display choices for user like exit, search for item, add own item.
def display_menu():
    print()
    print('Menu')
    print('---------------------------')
    print('0. Quit')
    print('1. Add item')
    print('2. Display receipt')
    print('3. Save and Display receipt')
    print()

    # Get the user's choice.
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if choice < QUIT or choice > SAVE_DISPLAY_RECEIPT:
                choice = int(input('That is not an option, please enter a number between 0 and 3: '))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    # Validate the choice.

    # return the user's choice.
    return choice


def add_items():
    print("0. To Quit")
    goods = my_inventory.get_base_inventory().items()
    my_index = 0
    print("10. Add your own items\n")
    while True:
        try:
            choice = int(input('Select an item by number to add to your cart: '))
            break
        except ValueError:
            print("Please enter in the number corresponding to the item you want. ")
    if choice <= len(list(goods)) and choice != 0:
        for k, v in goods:
            my_index += 1
            if my_index == choice:
                NAME.append(k)
                PRICE.append(v)
        while True:
            try:
                QUANTITY.append(int(input('Please enter in the quantity for {}: '.format(NAME))))
                my_inventory.set_quantity(QUANTITY)
                break
            except ValueError:
                print("You must enter in a number")
        print("You choose {} {}".format(NAME, PRICE))
        my_inventory.set_product_name(NAME)
        my_inventory.set_product_price(PRICE)
    elif choice == 10:
        NAME.append(input('Please enter the name of your first item: '))
        my_inventory.set_product_name(NAME)
        while True:
            try:
                PRICE.append(float(input('Please enter in the price: ')))
                my_inventory.set_product_price(PRICE)
                break
            except ValueError:
                print("Should be a number ")
        while True:
            try:
                QUANTITY.append(int(input('Please enter in the quantity: ')))
                my_inventory.set_quantity(QUANTITY)
                break
            except ValueError:
                print("Please enter in the quantity, it should be a number ")
    elif choice == QUIT:
        quit_program()


# Generate receipt, do calculations, and save to a file.
# Here we will call Inventory class to calculate subtotal, total price and save and display receipt.
# Have option to return to main menu.
# Put try, except, finally here. The finally will print even if unable to save it.

def save_receipt():
    pass


# display receipt of purchase, maybe as text and GUI.
# Here we will call Inventory class to calculate subtotal, total price and save and display receipt.
# Have option to return to main menu.
def display_receipt():
    pass


if __name__ == '__main__':
    main()



