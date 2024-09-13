

class Engine:
    
    def __init__(self,horse_power):
        self.horse_power = horse_power

class Wheel:

    def __init__(self,wheel_size):
        self.wheel_size = wheel_size

class Car:

    def __init__(self,model,horse_power,wheel_size):
        self.model = model
        self.engine=Engine(horse_power) # ***
        self.wheel = Wheel(wheel_size)  # ***

    def display(self):
        return f"Model:{self.model} - Horse Power {self.engine.horse_power} (hp) - Wheel Size: {self.wheel.wheel_size} inch"

car=Car('Mustang',500,21)

print(car.display())
