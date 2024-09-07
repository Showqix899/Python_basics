# if it's looks like a duck,quack like duck then it is a duck

class Animal:

    alive=True

class Cat(Animal):

    def speak(self):
        print("Meow")
class Dog(Animal):
    def speak(self):
        print("woof")
class Car:
    alive=False
    def speak(self):
        print("honk")

objects=[Cat(),Dog(),Car()]

for obj in objects:
    obj.speak()
    print(obj.alive)