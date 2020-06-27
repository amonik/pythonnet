class Product:
    """ The __ allows these variables to be only used inside class (private variables)"""
    def __init__(self):
        self.__product = {}

    """ The set_product method sets the product_name attribute"""
    def set_product_name(self, product):
        self.__product = product

    """ The get_product_name returns the product_name attribute"""
    def get_product_name(self):
        return self.__product

    def __str__(self):
        return format(self.__product)


class OrderLine:
    def __init__(self, product):
        self.__product = product
        self.__quantity = 0
        self.__product_price = ""

    def set_product(self, product):
        self.__product = product

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_product_price(self, total):
        self.__product_price = total

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_product_price(self):
        return self.__product_price

    def get_line_total(self):
        return self.get_product_price() * self.get_quantity()

    def __str__(self):
        return "{:13} {:5} {:8} {}".format(self.get_product(), str(self.get_quantity()),
                                           str(self.get_product_price()), str(self.get_line_total()))


class Address:
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__address = ""

    """All the getters and setters are used because we use private variables with __"""
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def get_first_name(self):
        return self.__first_name

    def get_address(self):
        return self.__address

    def get_last_name(self):
        return self.__last_name

    def __str__(self):
        return "{} {} {}\n".format(self.get_first_name(), self.get_last_name(), self.get_address())


class Order:
    def __init__(self, order_id):
        self.__customer_order = []
        self.__ship_to = ""
        self.__bill_to = ""
        self.__grand_total = 0
        self.__order_id = order_id

    def set_customer_order(self, customer_order):
        self.__customer_order = customer_order

    def set_ship_to(self, ship_to):
        self.__ship_to = ship_to

    def set_bill_to(self, bill_to):
        self.__bill_to = bill_to

    def set_grand_total(self, grand_total):
        self.__grand_total = grand_total

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_customer_order(self):
        return self.__customer_order

    def get_ship_to(self):
        return self.__ship_to

    def get_bill_to(self):
        return self.__bill_to

    def get_grand_total(self):
        return self.__grand_total

    def get_order_id(self):
        return self.__order_id

    def __str__(self):
        return "\nOrder #: {}\t\tOrder Total: {}\nProduct Name\tQty\tUnit Price\tTotal"\
            .format(self.get_order_id(), self.get_grand_total())
