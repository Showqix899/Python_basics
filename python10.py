#function
def my_function():
  print("Hello from a function")
my_function()

def writeAName(fName,LName):
  print(fName + ' ' + LName)

writeAName("Tom","Cruise")

# n numbers of argument
def children(*kid):
  print(kid[2])
children("eni","mini","myni","moo")