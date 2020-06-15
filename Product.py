class Product:
    """ Initialize the variables product_name and product_price."""
    """ It accepts an argument for product_name and product_price"""
    """ The __ allows these variables to be only used inside class (private variables)"""
    def __init__(self):
        self.__product_name = ''
        self.__product_price = 0

    """ The set_product method sets the product_name attribute"""
    def set_product_name(self, product_name):
        self.__product_name = product_name

    """ The get_product_name returns the product_name attribute"""
    def get_product_name(self):
        return self.__product_name

    """" The set_products_price sets the product_price attribute"""
    def set_product_price(self, product_price):
        self.__product_price = product_price

    """ The get_product_price returns the product_price attribute"""
    def get_product_price(self):
        return self.__product_price

    """ The calculate_tax returns the tax rate of 8.25% on the product"""
    def calculate_tax(self):
        return 0.0825 * Product.get_product_price(self)

    """" The get_total_price returns the tax of each product plus the price of the product"""
    def get_total_price(self):
        return round(Product.get_product_price(self) + Product.calculate_tax(self), 2)

    """Returns the objects state as a string"""
    def __str__(self):
        return "The total price with tax for {} is: ${} \n".format(
            Product.get_product_name(self),
            Product.get_total_price(self))


