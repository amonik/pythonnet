"""
Take the input of the package weight from user as float.
Create a if, elif, else condition.
Display the shipping rate.
"""

weight = input("Please enter in the weight of your package: ")
weight_package = float(weight)
shipping_charges = 0

if weight_package <= 2:
    shipping_charges = 1.50
elif 2 < weight_package <= 6:
    shipping_charges = 3.00
elif 6 < weight_package <= 10:
    shipping_charges = 4.00
elif weight_package > 10:
    shipping_charges = 4.75

print("Your shipping rate is {}".format(shipping_charges, '.2g'))
