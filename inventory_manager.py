import inventory
import pickle
import sys

# Global constants for menu choices
ADD_ITEM = 1
DELETE_ITEM = 2
DISPLAY_RECEIPT = 3
SAVE_DISPLAY_RECEIPT = 4
QUIT = 5


# Call all functions below from this main.
def main():
    # Initialize a variable for the user's choice.
    choice = 0
    choice = display_menu()
    if choice == SEARCH_ITEM:
        print("Displaying Item Search..")


# Open the inventory file that has item name and price.
def load_items():
    pass


# Display choices for user like exit, search for item, add own item.
def display_menu():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Add item')
    print('2. Delete item')
    print('3. Display receipt')
    print('4. Save and Display receipt')
    print('5 Quit')
    print()

    # Get the user's choice.
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if choice == 5:
                print("Exiting program...")
                sys.exit(0)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    # Validate the choice.

    # return the user's choice.
    return choice


# Display a list of items the user buy or give option to add own items with price.
# Here will will call the Inventory class.
# If they want to add from list it will assign items to get_product_name and get_product_price
# then ask the user for quantity and assign this to quantity.
# If they want to add items the user will be asked for all items.
# Have option to return to main menu.
def add_items():
    pass


# Allow user to delete item.
# Have option to return to main menu.
def delete_item():
    pass


# Generate receipt, do calculations, and save to a file.
# Here we will call Inventory class to calculate subtotal, total price and save and display receipt.
# Have option to return to main menu.
def save_receipt():
    pass


# display receipt of purchase, maybe as text and GUI.
# Here we will call Inventory class to calculate subtotal, total price and save and display receipt.
# Have option to return to main menu.
def display_receipt():
    pass


if __name__ == '__main__':
    main()



