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
    def subtotal(self):
        for i in range(len(Inventory.get_quantity(self))):
            print(Inventory.get_quantity(self)[i] * Inventory.get_product_price(self)[i])

    """" The get_total_price returns the tax of each product plus the price of the product
    def get_total_price(self):
        return round(Inventory.subtotal(self) * 1.0825, 2)
"""
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

    """Returns the objects state as a string
    def __str__(self):
        return "The total price with tax for {} is: ${} \n".format(
            Inventory.get_product_name(self),
            Inventory.get_total_price(self))
    """


