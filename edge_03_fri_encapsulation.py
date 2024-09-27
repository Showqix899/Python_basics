class Account:

    #initialising the constructor
    def __init__(self,balance):
        self.__balance=balance

    #defining the method to display the balance
    def get_balance(self):
        print(f'the amount is {self.__balance}')

    #updating the balance
    def update_balance(self,new_balance):
        self.__balance=new_balance

assets=Account(9000)

# print(assets.__balance)

#getting the balance
assets.get_balance()

#updating the balance
assets.update_balance(8000)

#getting the balance
assets.get_balance()