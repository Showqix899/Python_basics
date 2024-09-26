

import random

#assigning flag to True to run the game
flag=True

#while loop will run till the flag is True
while(flag):
    #ask to generate a random number from 1 - 100 or to quit the game
    print('1.Generate a random number to guess(1-100)')
    print('2.Quit the game')

    #taking the selected option
    selected_option=input('Select: ')    
    
    #checking the selected option
    if selected_option=='1':

        #generating a random number
        random_number=random.randint(1,100)

        #alerting about the limit
        print("You have seven attempts to guess the number. Goodluck")

        #seting the range 1 to 7 using for loop
        for i in range(1,8):

            #giving the input   number and checking the if it is valid
            try:
                answere=int(input("Enter Your Number(1-100): "))
            except ValueError:
                #if it is invlaid 
                print('You entered an invalid number, please try again')
                continue
            print(random_number)
            #checking if the input is 
            if answere>=0 and answere<=100:

                #checking the answere guessed number
                if random_number==answere: #if matched
                    print("congratulation, You guessed it!!!!")
                    break

                #for warning
                elif random_number != answere and i<7:

                    #if wrong answere in one attempt
                    print('Wrong, please guess again!')

                    #showing how many attempts left
                    print(f'you have {7-i} attempts left')

                #if not matched
                else:
                    #if unsuccesfull to guess after all the attempts
                    if i==7:
                        print(f'sorry loser,better luck next time. the secret number was- {random_number}')

                    #if wrong answere in one attempt
                    else:
                      print('please, guess again!')

            #if some one entered a value less then 1 or more than 100
            else:
                print('Please enter a value between 1 to 100')
           
    
    else:
        #assigning flag to false to quit the game
        flag=False

    

    