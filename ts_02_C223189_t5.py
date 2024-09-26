# Get the number from the user
number = int(input("Enter the number: "))

# Initialize a counter starting from 1
counter = 1

# Loop through the range of 1 to 10 (inclusive)
for counter in range(1, 11):
    
    # Check if the counter is a multiple of 3
    if counter % 3 == 0:
        continue  # Skip this iteration if it's a multiple of 3
    
    # Print the multiplication table for the current counter
    print(number, '*', counter, '=', number * counter)
