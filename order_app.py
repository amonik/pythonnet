from muliclass import Product, Address, OrderLine, Order
import random


product_1 = Product()
product_1.set_product_name({"Apples": 2.00})

product_2 = Product()
product_2.set_product_name({"Sushi": 8.00})

product_3 = Product()
product_3.set_product_name({"Corn": 1.00})

ship_address_a = Address()
ship_address_a.set_first_name("Stephanie")
ship_address_a.set_last_name("Tian")
ship_address_a.set_address("555 Monkey Way, Silly, TX 70055")

billing_address_a = Address()
billing_address_a.set_first_name("Daniel")
billing_address_a.set_last_name("Chen")
billing_address_a.set_address("111 Flip St, Nas, TX 70022")

order_line_1 = OrderLine(product_1)
order_line_1.set_quantity(3)
for key, value in product_1.get_product_name().items():
    order_line_1.set_product(key)
    order_line_1.set_product_price(value)
# print(order_line_1)

order_line_2 = OrderLine(product_2)
order_line_2.set_quantity(2)
for key, value in product_2.get_product_name().items():
    order_line_2.set_product(key)
    order_line_2.set_product_price(value)
# print(order_line_2)

order_line_3 = OrderLine(product_3)
order_line_3.set_quantity(8)
for key, value in product_3.get_product_name().items():
    order_line_3.set_product(key)
    order_line_3.set_product_price(value)
# print(order_line_3)

order_num = Order(random.randint(1, 500))
order_num.set_ship_to(ship_address_a)
order_num.set_bill_to(billing_address_a)
order_num.set_grand_total(order_line_1.get_line_total() +
                          order_line_2.get_line_total() +
                          order_line_3.get_line_total())

my_list = [order_line_1, order_line_2, order_line_3]

order_num.set_customer_order(my_list)

print(order_num)
for order in order_num.get_customer_order():
    print(order)
print("Ship To: {}Bill To: {}".format(order_num.get_ship_to(), order_num.get_bill_to()))



