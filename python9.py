####dictionary
thisdict = {                ## "key":"value"
  "brand": "Ford",          ## note: duplicate value not allowed
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#indexing
print(thisdict["brand"])
print(len(thisdict)) # length

x=thisdict.keys() # return a list of keys
y=thisdict.values()  # return a list of values
print(x)
print(y)
##updating
thisdict["year"]=1969
print(thisdict)

thisdict["color"]="Black" # added another key and it's vlaue
print(thisdict)
# remove items
thisdict.pop("model")
print(thisdict)
thisdict.clear() ## clear the entire dictionary
print(thisdict)

company={
    "Netflix":"Entertainment",
    "Google":"Tech",
    "Cucabura":"Sports",
    "Raymond":"Clothing"
}
for i in company:
    print(f"{i} : {company[i]}")
#copy
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict2.copy()
print(mydict)
#nested Dictionary
myFamily={
    "child1":{
        "name":"Stefen Salvator",
        "age":"168"
    },
    "child2":{
        "name":"Demon Salvator",
        "age":"168"
    },
    "child3":{
        "name":"Klaus Michelson",
        "age": "1000"
    },
    "child4":{
        "name":"Elijah Michelson",
        "age":"1000"
    }
}
# traverse through the nested dictionary
for i,obj in myFamily.items():
    print(i)
    for j in obj:
        print(j +' :'+obj[j])