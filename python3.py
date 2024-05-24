#string manipulation
print("it's alright") # direct
string = "Lord of The ring" # store in a variable
print(string)
#multiple line 
lorem ="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(lorem)
#string indexing

a="Hello,World"
print(a[1]) #'e' index = 1
#slicing string
print(a[0:6]) # 'H e l l o ,'
              #  0 1 2 3 4 5
              # position zero to 6 (here 6 is not included)
print(a[2:5]) # 'llo'
              # position 2 to position 5 (here 5 is not included )


print(a[2:]) # 'llo, world'
#negative indexing (-1 is the starting index)
print (a[-5:-2])
#modify index
upperCase=a.upper() # converting hole string to uppercase
print(upperCase)
lowerCase=a.lower() # coverting hole string to lowercase
#Removing any whiteSpaces
line= "Harry Potter And The Deathly Hollows"
print(line.strip()) #removing the white spaces
                 #output: HarryPotterAndTheDeathlyHollows
#replacing string
b="hello"
print(b.replace("h","j")) # output: "jello"

#spliting string
st= "Harry,Potter,And,The,Deathly,Hollows"
print(line.split(",")) # return a list :['Harry','Potter','And','The','Deathly','Hollows']
#concatenation of string
first="hello"
second="world"
full=first+second
print(full) #output: helloworl

full2=first + " " + second # to add a white space
print(full2) #output: hello world
#formate String
age=21
name=f"i am Showqi and i am {age}" # fstring
print(name) #output: i am Showqi and i am 21


