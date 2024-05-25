### tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple)) # length of a tuple
#one item tuple
tup=("axe",) # there must be ',' after that one element
t=("hello",1,1.1111,True,False) # tuple can hold defferent data types
print(t)
#indexing of a tuple
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[0]) # this will print the first element of this tuple 
print(fruits[-1]) # this will print the last element of this tuple. this called negative indexing

print(fruits[:4]) # this will print 0 to 4 excluding 4
print(fruits[2:]) # this will print index 2 to till the last index

#conditons in tuple
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits tuple")

# updating a tuple
# note: Tuples are immutable. if it's realy have to be done first type cast the tuple into list
#       then update the list or change it then type cast the list back to tuple
x = ("apple", "banana", "cherry")

y=list(x) # converted into list
y[1]="Resberry" # updated the list
x=tuple(y) # converted back to typle
print(x)
## ***Note: you can also performe remove(), appende(), extende() etc


##loops
for i in x:
  print(i)