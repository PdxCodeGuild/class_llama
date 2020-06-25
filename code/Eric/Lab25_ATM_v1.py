import random


class Account:
    
    def __init__(self):

    # Function to deposite amount 
def deposit(self): 
        amount = float(input("Enter amount to be deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:", amount) 

    # Function to withdraw the amount 
def withdraw(self): 
        amount = float(input("Enter amount to be withdrawn: ")) 
        if self.balance >= amount: 
            self.balance -= amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 

def display(self): 
        print("\n Net Available Balance =", self.balance) 


           

    