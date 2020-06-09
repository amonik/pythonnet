"""
Write function that takes one floating point number of Temp in F.
The function should then convert this into C and display it.
Outside of the function the code needs to use the function and
display temp F 0 to 20 and C equivalents in a table. Use a While loop.
"""


def fahrenheit_to_celsius(f):
    c = (f - 32) * (5/9)
    return c


temp = 0
print("{} {}".format("FAHRENHEIT", "CELSIUS"))
while 20 >= temp >= 0:
    print("{:^10} {:^5}".format(temp, round(fahrenheit_to_celsius(temp), 2)))
    temp += 1
