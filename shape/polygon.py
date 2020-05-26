# This is the main class that the others import
class Polygon:
    """declare private variables, there is no constructor(__init__)"""
    __width = None
    __height = None

    def set_value(self, width, height):
        """ Set the private variables width and height of the shape"""
        self.__width = width
        self.__height = height

    def get_width(self):
        """ Use getter to get width. Need to do this because it is private"""
        return self.__width

    def get_height(self):
        """ Use getter to get height. Need to do this because it is private"""
        return self.__height



