##lists

mylist=["apple","banana","cherry"] # note:list allow duplicate value

print(mylist)
print(len(mylist)) # printing the length of the list

# list can hold different data types all together
list1=["abc",89,True,3.33]
print(list1)

#indexing a list
thisList= ["Steven Smith","Joe Root","Pet Cummins","Joss Buttler","ken Williamson","Jimme Nissam"]
print(thisList[1]) #output: Joe Root
# negative indexing
print(thisList[-1]) #output: Jimme Nissam
#range of List
print(thisList[2:5]) #output: Pet Cummins,Joss Buttler,Ken Williamson

print(thisList[:4]) # this will print index 0 to 3 exluding the index four value
                    # output: Steven Smith Joe Root Pet Cummins Joss Buttler
##conditional statement in list
if "Joe Root" in thisList:
    print("Joe Root in the List")

#list Mnipulation
list2= ["Messi","Toni Cross","Martinez","Pedro"]
list2[1]="julian Alvarez" # it will replace value at index one
print(list2)

list2[2:4]=["enzo Farnandez","Emiliano Martinez"] # it will replace values of index 2:4 excluding 4
print(list2) 
#inserting
list3=["Samsung","Apple","Asus","MSI","Gigabyte","Dell","HP","Alien"]
print(len(list3))
list3.insert(4,"Razer")
print(list3)
print(len(list3))
#adding list item
li=["samsung","apple","realme","xioami","nothing","google"]
li.append("Oppo")
print(li)
#extend
li1=[1,2,3,4]
li2=[5,6,7,8]
li1.extend(li2)
print(li1)
goat=["messi","ronaldo"]
goat.remove("ronaldo") # also can be done :goat.remove(goat[1])
print(goat)
#pecified index value removing
nums=[1,2,3]
nums.pop(2)
print(nums)

#loops in list

course=["web dev","machine learning","cybersecurity","data science","software engineering"]
for x in course:
    print(x)
#using index
for i in range(len(course)):
    print(course[i])

# sorting
number=[1,3,2,6,5,4,8,7]
number.sort()
print(number)
number.sort(reverse=True) # reverse
print(number)
# list joining
e=[1,2,3]
f=[5,6,7]
g=e+f
print(g)
#clear
g.clear()
print(g)