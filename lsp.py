#species class

class Species:
    pass

#i  
class IQ(Species):
    
    def brain(self):
        print('got higher iq')

class Human(IQ):
    pass

class Snails(Species):
    pass

human=Human()

human.brain() # got higher iq

snails=Snails()

#--------------------------------

#defining the parent class
class Vehicle:

    pass
#is the vehicle divable
class Drivable(Vehicle):

    def drive(self):
        pass

#is the vehicle Flyable
class Flyable(Vehicle):
    def fly(self):
        pass

#creating car class inheriting vehicle and Driveable
class Car(Vehicle,Drivable):

    def drive(self):
        print("Car can drive")

#creating airplane class inheriting vehicle and Flyable
class Airplane(Vehicle,Flyable):

    def fly(self):
        print("Airplane can fly")

#creating objects 
car=Car()
car.drive()

airplane=Airplane()
airplane.fly()


