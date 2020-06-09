"""
Take the input of the package weight from user as float.
Ask the user again if input is not a digit.
Create a if, elif, else condition.
Display the shipping rate.
"""
shipping_charges = 0

while True:
    try:
        weight_package = float(input("Please enter in the weight of your package: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

if weight_package <= 2:
    shipping_charges = 1.50
elif 2 < weight_package <= 6:
    shipping_charges = 3.00
elif 6 < weight_package <= 10:
    shipping_charges = 4.00
elif weight_package > 10:
    shipping_charges = 4.75

print("Your shipping rate is ${:.2f}".format(shipping_charges))
