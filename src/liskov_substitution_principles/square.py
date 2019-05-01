from src.liskov_substitution_principles.rectangle import Rectangle


class Square(Rectangle):
    ''' This example violates LSP, because even though Square follows
    Rectangle contract, the method's body does not.
    '''

    def __init__(self, widthHeight):
        self.width = widthHeight
        self.height = widthHeight

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        self.__width = width
        self.__height = width

    @height.setter
    def height(self, height):
        self.__height = height
        self.__width = height

    def get_area(self):
        return self.width * self.height
