from shape.square import Square
from shape.triangle import Triangle
"""Import the file_location.filename and class.
This need to import square and triangle to run.
Everything will be run from the main class.
"""

s1 = Square()
"""Call an instance of the square class"""
s1.set_value(8, 54)
"""Set the values of the square"""
print(s1.get_area())
"""print the area"""


s2 = Triangle()
"""Call an instance of the triangle class"""
s2.set_value(35, 89)
print(s2.get_tri_area())
