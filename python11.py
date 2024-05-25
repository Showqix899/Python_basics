#class and objects
class myClass:
    x=5

y=myClass()
print(y.x)
# using of _init_()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#using of _str_()
class Movie:
    def __init__(self,name,boxOffice) -> None:
      self.name=name
      self.boxOffice=boxOffice
    
    def __str__(self) -> str:
      return f"Name:{self.name} - boxoffice: {self.boxOffice}M $"
    
m=Movie("DeadPool",678)
print(m)
#using Traditional Function
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person2("John", 36)
p1.myfunc()
#inheritance
class Animal:
  alive=True
  def myFunc(self):
    print("animal is alive")

class Tiger(Animal):
  pass
class Rabbit(Animal):
  pass

T=Tiger()
R=Rabbit()
print(T.alive)
print(R.alive)
T.myFunc()
R.myFunc()

### inheritance with argument
class EPL:
  def __init__(self,name):
    self.name=name
    print(f"Team: {self.name}")
class ManchesterCity(EPL):
  pass
class Tottenham(EPL):
  pass
class AstonVilla(EPL):
  pass

team1 = ManchesterCity("Manchester City")
team2 = Tottenham("Tottenham Hotspur")
team3 = AstonVilla("Aston Villa")
    
