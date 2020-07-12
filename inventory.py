class Inventory:
    """ Initialize the variables product_name and product_price."""
    """ It accepts an argument for product_name and product_price"""
    """ The __ allows these variables to be only used inside class (private variables)"""

    def __init__(self):
        self.__product_name = []
        self.__product_price = []
        self.__product_quantity = []
        self.__base_inventory = {}

    """ The set_product method sets the product_name attribute"""

    def set_product_name(self, product_name):
        self.__product_name = product_name

    """" The set_products_price sets the product_price attribute"""

    def set_product_price(self, product_price):
        self.__product_price = product_price

    def set_quantity(self, quantity):
        self.__product_quantity = quantity

    """ The get_product_name returns the product_name attribute"""

    def get_product_name(self):
        return self.__product_name

    """ The get_product_price returns the product_price attribute"""

    def get_product_price(self):
        return self.__product_price

    def get_quantity(self):
        return self.__product_quantity

    """ The calculate_tax returns the tax rate of 8.25% on the product"""

    def line_total(self):
        for i in range(len(Inventory.get_quantity(self))):
            print("{} - {} at {} line total is: {}".format(self.get_quantity()[i], self.get_product_name()[i],
                                                           self.get_product_price()[i],
                                                           round(self.get_quantity()[i] *
                                                                 self.get_product_price()[i], 2)))

    def get_base_inventory(self):
        self.__base_inventory = {'Bread': 2.49,
                                 'Milk': 5.79,
                                 'Eggs': 6.99,
                                 'Yogurt': 8.49,
                                 'Oranges': 0.39}
        my_index = 0
        for k, v in self.__base_inventory.items():
            my_index += 1
            print("{}. {}  {}".format(my_index, k, v))
        return self.__base_inventory


class Total:
    def __init__(self):
        pass

    def calculate_tax(self):
        pass

    def show_line_total(self):
        pass

    def display_grand_total(self):
        pass

