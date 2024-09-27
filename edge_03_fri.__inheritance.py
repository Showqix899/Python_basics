#defining the vehicle class

class Vehicle:
    
    def __init__(self,model,year,wheels):
        self.model = model  
        self.year=year
        self.wheels=wheels


#defining Car class inheriting Vehicle:

class Car(Vehicle):

    def __init__(self,doors):
        super().__init__(self,wheels=4)
        self.doors=doors

    def show_car_info(self):
        print(f'{self.model} has {self.wheels} and {self.doors}')
    

#defining Bike class inheriting Vehicle

class Bike(Vehicle):

    def __init__(self,cornaring_angle):
        super().__init__(self,wheels=2) # Calling the constructor of the parent class
        cornaring_angle="is available"

    def show_bike_info(self):
        
         print(f'{self.model} has {self.wheels} and {self.doors}')


# Defining the Vehicle class
class Vehicle:
    def __init__(self, model, year, wheels):
        self.model = model  # Attribute for the vehicle model
        self.year = year    # Attribute for the vehicle year
        self.wheels = wheels  # Attribute for the number of wheels


# Defining the Car class, inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, model, year, doors):
        super().__init__(model, year, wheels=4)  # Pass model, year to Vehicle, set wheels to 4
        self.doors = doors  # Additional attribute for Car

    def show_car_info(self):
        print(f'{self.model} from {self.year} has {self.wheels} wheels and {self.doors} doors')


# Defining the Bike class, inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, model, year, cornering_angle):
        super().__init__(model, year, wheels=2)  # Pass model, year to Vehicle, set wheels to 2
        self.cornering_angle = cornering_angle  # Additional attribute for Bike

    def show_bike_info(self):
        print(f'{self.model} from {self.year} has {self.wheels} wheels and a cornering angle of {self.cornering_angle} degrees')


# Example usage

# Creating a Car object
my_car = Car("Toyota Camry", 2020, 4)
my_car.show_car_info()  # Output: Toyota Camry from 2020 has 4 wheels and 4 doors

# Creating a Bike object
my_bike = Bike("Yamaha R1", 2021, 45)
my_bike.show_bike_info()  # Output: Yamaha R1 from 2021 has 2 wheels and a cornering angle of 45 degrees

