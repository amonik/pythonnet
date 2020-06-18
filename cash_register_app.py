import product


def main():
    get_total = []
    total = 0

    p1 = product.Product()
    p1.set_product_name("Apples")
    p1.set_product_price(4.79)
    get_total.append(p1.get_product_price())
    print(p1)

    p2 = product.Product()
    p2.set_product_name("Pizza")
    p2.set_product_price(5.99)
    get_total.append(p2.get_product_price())
    print(p2)

    p3 = product.Product()
    p3.set_product_name("Hummus")
    p3.set_product_price(5.79)
    get_total.append(p3.get_product_price())
    print(p3)

    for price in get_total:
        total += price

    print("Grand Total the customer needs to pay is: {}".format(total))


if __name__ == '__main__':
    main()

