from abc import ABC,abstractmethod

# #defining a player class 
# class Player:

#     #implementing abstruct method
#     @abstractmethod
#     def player(self):
#         pass

# class Football_player(Player):

#     #defining the constructor
#     def __init__(self,name):
#         self.name=name
#     # defining the abstruct method  
#     def player(self):
#         print(f'{self.name} is playing football')

# football_player=Football_player('messi')

# football_player.player()


#-----------------------------
#defining the parent class

class Shape:

    #implementing the abstruct method
    @abstractmethod
    def area(self):
        pass

#defining the subclass Cicle

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.1416*self.radius**2
    
#defining the subclass Rectangle

class Rectangel(Shape):

    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    

#creating a object for Cicle class
circle=Circle(5)

area_of_circle=circle.area()

#creating a object for Rectangle
rectangle=Rectangel(6,8)

area_of_rectangle=rectangle.area()


#showing the result
print(f'the area of the circle is {area_of_circle}')
print(f'the area of the rectangle is {area_of_rectangle}')


        