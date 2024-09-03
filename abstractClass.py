# if any children class inherite from abstract class(Vehicle)

# the children classes(Car,....) only can use the methods described in Parent class(Vehicle)
#if u try any other method it will give error



from abc import ABC ,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

    
class Car(Vehicle):

    def go(self):
        print("Car is moving")
    
    def stop(self):
        print("Car is stopped")

car=Car()
car.go()
car.stop()


class Motorcycle(Vehicle):
    def go(self):
        print("Motorcycle is moving")

    def stop(self):
        print("Motorcycle is stoped")

honda=Motorcycle()

honda.go()
honda.stop()


            
        