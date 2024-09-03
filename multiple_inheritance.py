# Animal class is the Base or root class
# Prey and Predator class inherite the methods from the Animal class

# Rabit,Wolf and Fish inherite the mehtods of Prey and Predator class and 
# Prey and Predator is inheriting from Animal as a result Rabit,Wolf and Fish
# is also can inheriting the methods of Animal class

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} is sleeping')


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing!")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")


class Rabit(Prey):
    pass
class Wolf(Predator):
    pass
class Fish(Prey,Predator):
    pass


rabit=Rabit('bugs')
rabit.flee()
rabit.sleep()


wolf=Wolf('wolfi')
wolf.hunt()
wolf.sleep()
#Fish is a mix of both prey and predator so it can do both
fish=Fish('fishy')
fish.flee()
fish.hunt()

