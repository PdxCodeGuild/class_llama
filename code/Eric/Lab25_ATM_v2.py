class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Welcome to the Best ATM Ever!") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Available Balance=",self.balance) 
  
  
# create a class object 
s = Bank_Account() 
   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 