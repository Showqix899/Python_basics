# Class for fuel efficiency calculation
class FuelEfficiencyCalculator:
    def __init__(self, miles, fuel):
        # Initialize with miles driven and fuel consumed
        self.miles = miles
        self.fuel = fuel

    def car_fuel_efficiency_calculator(self):
        # Return miles per gallon (MPG)
        return self.miles / self.fuel

# Class for Car, inheriting from FuelEfficiencyCalculator
class Car(FuelEfficiencyCalculator):
    def __init__(self, model, fuel_efficiency, miles, fuel):
        super().__init__(miles, fuel)
        self.model = model
        self.fuel_efficiency = fuel_efficiency

    def drive(self):
        print(f'{self.model} is being driven')

    def display_fuel_efficiency(self):
        # Show car model and its fuel efficiency
        print(f'{self.model} has a fuel efficiency of {self.car_fuel_efficiency_calculator()} miles per gallon.')

# Create an instance of the Car class
my_car = Car("Honda Civic", 30, 300, 10)

# Call the drive method
my_car.drive()  # Output: Honda Civic is being driven

# Display the fuel efficiency of the car
my_car.display_fuel_efficiency()  # Output: Honda Civic has a fuel efficiency of 30.0 miles per gallon.

