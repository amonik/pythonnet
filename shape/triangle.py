from shape.polygon import Polygon
"""Import the file_location.filename and class"""


class Triangle(Polygon):
    """returns area of a triangle
    Inheritance (Inherits all the variables for the Polygon class)"""
    def get_tri_area(self):
        return int(self.get_width() * self.get_height() * 0.5)
