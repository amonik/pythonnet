import inventory
import sys

# Global constants for menu choices
ADD_ITEM = 1
DISPLAY_RECEIPT = 2
QUIT = 0
MY_INVENTORY = inventory.Inventory()
NAME = []
QUANTITY = []
PRICE = []


def quit_program():
    print("Exiting program...")
    sys.exit(0)


def return_main_menu():
    while True:
        try:
            print("Would your like to return to the main menu?")
            response = int(input("0. Exit\n1. Main Menu:\n"))
            return response
        except ValueError:
            print("That is not a valid options. Please enter 0  or 1")


# Call all functions below from this main.
def main():
    # Initialize a variable for the user's choice.
    choice = display_menu()
    if choice == ADD_ITEM:
        print("\nAvailable Items")
        print("_______________")
        add_items()
        display_receipt()
        my_response = return_main_menu()
        if my_response == 1:
            return main()
        elif my_response == 0:
            quit_program()
    elif choice == QUIT:
        quit_program()
    elif choice == DISPLAY_RECEIPT:
        display_receipt()
        my_response = return_main_menu()
        if my_response == 1:
            return main()
        elif my_response == 0:
            quit_program()


# Display choices for user like exit, search for item, add own item.
def display_menu():
    print()
    print('Menu')
    print('---------------------------')
    print('0. Quit')
    print('1. Add item')
    print('2. Display receipt')
    print()

    # Get the user's choice.
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if choice < QUIT or choice > DISPLAY_RECEIPT:
                choice = int(input('That is not an option, please enter a number between {} and {}: '
                                   .format(QUIT, DISPLAY_RECEIPT)))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    # return the user's choice.
    return choice


def add_items():
    print("0. To Quit")
    goods = MY_INVENTORY.get_base_inventory().items()
    given_goods = len(list(goods))
    my_index = 0
    print("{}. Add all items to the cart.".format(given_goods + 1))
    print("{}. Add your own items.\n".format(given_goods + 2))
    while True:
        try:
            choice = int(input('Select an item by number to add to your cart: '))
            break
        except ValueError:
            print("Please enter in the number corresponding to the item you want. ")
    if choice <= given_goods and choice != 0:
        for k, v in goods:
            my_index += 1
            if my_index == choice:
                NAME.append(k)
                PRICE.append(v)
                MY_INVENTORY.set_product_name(NAME)
                MY_INVENTORY.set_product_price(PRICE)
        while True:
            try:
                QUANTITY.append(int(input('Please enter in the quantity: ')))
                MY_INVENTORY.set_quantity(QUANTITY)
                break
            except ValueError:
                print("You must enter in a number")
        # MY_INVENTORY.set_product_name(NAME)
        # MY_INVENTORY.set_product_price(PRICE)
    elif choice == given_goods + 2:
        while True:
            try:
                number_of_items = int(input("Please enter in the number of items you want to add: "))
                break
            except ValueError:
                print("This should be a digit (number)!: ")
        for num in range(number_of_items):
            NAME.append(input('Please enter the name of the product {}: '.format(num + 1)))
            while True:
                try:
                    PRICE.append(float(input('Please enter in the price: ')))
                    MY_INVENTORY.set_product_price(PRICE)
                    break
                except ValueError:
                    print("Should be a number ")
            while True:
                try:
                    QUANTITY.append(int(input('Please enter in the quantity: ')))
                    MY_INVENTORY.set_quantity(QUANTITY)
                    break
                except ValueError:
                    print("Please enter in the quantity, it should be a number ")
        MY_INVENTORY.set_product_name(NAME)
    elif choice == given_goods + 1:
        for k, v in goods:
            NAME.append(k)
            PRICE.append(v)
            while True:
                try:
                    QUANTITY.append(int(input('Please enter in the quantity for {}: '.format(k))))
                    MY_INVENTORY.set_quantity(QUANTITY)
                    break
                except ValueError:
                    print("You must enter in a number")
            MY_INVENTORY.set_product_name(NAME)
            MY_INVENTORY.set_product_price(PRICE)
    elif choice == QUIT:
        quit_program()


def display_receipt():
    MY_INVENTORY.line_total()
    print(MY_INVENTORY.grand_total())


if __name__ == '__main__':
    main()



