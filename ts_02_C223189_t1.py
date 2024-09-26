#input the number to check if it is negative,positive or zero
number=int(input('Enter Your Number: '))

#checking if it is positive
if number > 0:
    print(f'{number} is positive ')
#checking if it is negative
elif number < 0:
    print(f'{number} is negative')
#checking if it is zero
else:
    print(f'{number} is zero')