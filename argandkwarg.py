##arbutrary arguments for non key values
def add(*args):
    total=0
    for i in args:
        total += i
    return total
print(add(1,2,3))

def show_names(*names):
    for i in names:
        print(i,end=" ")

show_names("Dr.","Spongebob","Harold","squirepants")
#arbutrary arguments for key values

def address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

address(street="989 meow street",
        House="Devils Tail",
        Zip="6966969")