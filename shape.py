class Shape :
    def draw (seft):
        raise NotImplementedError ("Subclass must implement abstract method")

class Circle (Shape) :
    def __init__(self,radius):
        self.radius = radius

    def draw(self):
        print("Drawing a circle with radius", self.radius)

class Rectangle (Shape) :
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print("Drawing a rectangle with width", self.width, "and height", self.height) 

def draw_shape(shapes):
    for  shape in shapes:
        print(shape.draw())

Circle = Circle(5)

Rectangle = Rectangle(4, 6)
shapes_to_draw = [Circle , Rectangle]
draw_shape(shapes_to_draw)

