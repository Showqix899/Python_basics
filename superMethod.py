#super function is used for call the parent class method

class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
        


class Circle(Shape):
    def __init__(self,color,is_filled, radius):
        super().__init__(color,is_filled)
        self.radius = radius
        print(f"the color of Circle is {color} and the radius {radius} and filled={is_filled}")

class Squre(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color,is_filled)
        self.width=width
        print(f"The color of Squre is {color} and the width is {width} and filled={is_filled}")

class Triangle(Shape):
    def __init__(self, color, is_filled,width,height):
        super().__init__(color,is_filled)
        self.width=width
        self.height=height
        print(f"The color of Squre is {color} and the width:height is {width}:{height} and filled={is_filled}")

        
circle=Circle('red',True,5)
square=Squre('blue',False,10)
triangle=Triangle('green',True,5,10)