# Input the number to print its multiplication table
number = int(input('Enter the number:'))

# Assigning 1 to a counter
counter = 1

# Printing multiplication table of the entered number
while counter < 11:
    # Display the result of number * counter
    print(number, '*', counter, '=', number * counter)
    counter += 1
