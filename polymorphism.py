
from abc import ABC,abstractmethod
class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.1416*self.radius

class Squre(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side*self.side

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
            return 0.5*self.base*self.height
    
class Pizza(Circle):
    def __init__(self,toppings,radius):
        self.toppings = toppings
        self.radius=radius
        super().__init__(radius)



shapes=[Circle(5),Squre(4),Triangle(3,5),Pizza('cheese',9)]


for shape in shapes:
    print(shape.area())