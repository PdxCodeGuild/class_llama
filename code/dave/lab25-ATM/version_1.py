"""
This program is an ATM that allows: checks balance, deposit, check withdraw(amount) and withdraws(amount)
"""

# create the ATM class
class Atm:

    # initialization function
    def __init__(self, balance=0):
        self.balance = balance

    ## Declare multiple functions for each actions
    
    # func that checks balance
    def check_balance(self, balance):
        return self.balance

    # func that adds amount to balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # func that checks account balance
    def check_withdrawl(self, amount):
        if self.balance >= amount:
            return f"AVAILABLE"
        else:
            return f"NOT AVAILABLE"


    # func that withdraws the amount requested and returns it
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

atm = Atm()
print(f"You're balance is: ${atm.check_balance(0)}") # 0 : pass
print(f"Deposited amount: ${atm.deposit(60)}")
print(f"The funds you requested are {atm.check_withdrawl(60)}")
print(f"Your account balance is: ${atm.withdraw(20)}")