### set
# Note: set is  unorderd (it will only work on "strings, charecter,").but integer will be ordered
myset={"apple","banana","cherry"}
print(myset)
#adding
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset2 = {"apple", "banana", "cherry"}

thisset2.add("orange")


print(thisset2)
#removing items
thisset2.remove("banana")
print(thisset2)
#random item remove
thisset2.pop()
print(thisset2)
#clear out the entire set
thisset2.clear()
print(thisset2)
#loops int set
y={"messi","ronaldo","rues"}
for i in y:
    print(i)
# set join
set1 ={1,2,3,4}
set2 ={5,6,7,8}
set=set1.union(set2) # also can be done: set = set1 | set2
print(set)
#multiple union
set3={9,10,11,12}
superset=set1.union(set2,set3)
print(superset)
#join set and tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#intersection
setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple"}

setZ = setA.intersection(setB) # also can be done:set3 = set1 & set2
print(setZ)
#difference
l={"google","Microsoft","Amazon"}
k={"Microsoft","Nvidia","Netflix"}
m=l-k
print(m)
#symmetric difference
set11 = {"apple", "banana" , "cherry"}
set22 = {"google", "microsoft", "apple"}

set33 = set11.symmetric_difference(set22)
print(set33)
