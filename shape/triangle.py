from shape.polygon import Polygon
from shape.shapes import Shapes
"""Import the file_location.filename and class"""


class Triangle(Polygon, Shapes):
    """returns area of a triangle
    Inheritance (Inherits all the variables for the Polygon class)"""
    def get_tri_area(self):
        return int(self.get_width() * self.get_height() * 0.5)
