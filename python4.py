###  conditions(if/else) ###
a=33
b=200
if b>a:
    print("b is greater than a")
x=1
y=1
if x>y:
    print("x is greater than y")
elif x==y:
    print("x and y are equal")

num1=1
num2=2


if num1>num2:
    print("num1 is greater than num2")
elif num1==num2:
    print("num1 and num2 are equal")
else:
    print("num2 is greater than num1")


#shorthand syntax
p=1
q=2
if p>q :print("p is greater than q") # if the condition true it will print 
print("p is greater than q") if p>q else print("q is greater than q")
# and 
aa=True
bb=True
if aa and bb:
    print("both is true")
else:
    print("both is false")
#or
cc=True
dd=False
if cc or dd:
    print("at least one of them true")
else:
    print("both of the are false")
