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
    def check_balance(self):
        pass

    # func that adds amount to balance
    def deposit(self, amount):
        pass

    # func that checks account balance
    def check_withdrawl(self, amount):
        pass

    # func that withdraws the amount requested and returns it
    def withdraw(self, amount):
        pass