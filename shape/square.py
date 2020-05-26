from shape.polygon import Polygon
"""Import the file_location.filename and class"""


class Square(Polygon):
    """returns area of a square
    Inheritance (Inherits all the variables for the Polygon class)"""
    def get_area(self):
        return self.get_width() * self.get_height()
