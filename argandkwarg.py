
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