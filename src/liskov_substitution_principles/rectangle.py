class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    def get_area(self):
        return self.width * self.height
