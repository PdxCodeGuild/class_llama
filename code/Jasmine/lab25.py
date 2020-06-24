'''
Let's represent an ATM with a class containing a balance property. A newly created account
 will default to a balance of 0. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it

'''
class bankaccount: 
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
        
    def checkwithdrawl(self, amount): 
        if self.balance >= amount:
            return True
        return False

    def withdrawl(self, amount):
        if self.checkwithdrawl(amount): #checks the amount is good for withdrawl
            self.balance = self.balance - amount
        else: 
            print("insufficent funds")
        return self.balance

    def checkbalance(self):
        return self.balance
        

        

