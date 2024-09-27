class Shape:
    def area(self):
        raise NotImplementedError("sublsljfldk")

class Cicle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.1416 *self.radius*self.radius
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2