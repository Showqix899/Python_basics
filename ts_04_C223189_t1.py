#creating a class for Person

class Person:
    def __init__(self, name, age):
        #assigning the person's name
        self.name = name
        #assigning the person's age
        self.age = age
    # defining a method to printe attributes
    def display_info(self):
        print(f'the persons name is {self.name} and the age is {self.age}')
    # defining a person to greet the person
    def greet(self):
        print(f'hello,how are you mr {self.name}')

    #defining a method to update age
    def update_age(self,age):
        self.age =age
        print(f'{self.name} updated age is {age}')

#creating a object of Person class

person_one=Person("messi",36)

#calling the method to display the person's info
person_one.display_info()
#calling the method to greet the person
person_one.greet()

#calling the method for update the age
person_one.update_age(37)