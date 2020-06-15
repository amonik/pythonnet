import product


def main():
    p1 = product.Product()
    p1.set_product_name("Apples")
    p1.set_product_price(4.79)
    print(p1.__str__())

    p2 = product.Product()
    p2.set_product_name("Pizza")
    p2.set_product_price(5.99)
    print(p2.__str__())

    p3 = product.Product()
    p3.set_product_name("Hummus")
    p3.set_product_price(5.79)
    print(p3.__str__())

    print("Grand Total the customer needs to pay is: {}"
          .format(p1.get_total_price() +
                  p2.get_total_price() + p3.get_total_price()))


main()

