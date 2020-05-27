from shape.polygon import Polygon
from shape.shapes import Shapes
"""Import the file_location.filename and class"""


class Square(Polygon, Shapes):
    """returns area of a square
    Inheritance (Inherits all the variables for the Polygon class)"""
    def get_area(self):
        return self.get_width() * self.get_height()
