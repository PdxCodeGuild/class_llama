"""
This program is an ATM that allows: checks balance, deposit, check withdraw(amount) and withdraws(amount)
"""

from os import system, name

# create the ATM class
class Atm:

    # initialization function
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    ## Declare multiple functions for each actions
    
    # func that checks balance
    def check_balance(self):
        return self.balance

    # func that adds amount to balance
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"You deposited: ${amount}")
        return self.balance

    # func that checks account balance
    def check_withdraw(self, amount):
        if self.balance >= amount:
            return f"AVAILABLE"
        else:
            return f"NOT AVAILABLE"

    # func that withdraws the amount requested and returns it
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"You withdrew: ${amount}")
        return self.balance

    # func that prints transacs list
    def print_transactions(self):
        for line in self.transactions:
            print(line)

    # func that performs a clear screen in the terminal
    def clear(self):
        
        # if statement to implement for Windows or Unix
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    # func that prompts user to press enter to continue. 
    def enter_to_continue(self):
        print()
        input("Press ENTER key to continue(ENTER) ")
        atm.clear()


atm = Atm()

# TESTS FOR Atm Class
print(f"You're balance is: ${atm.check_balance()}") # 0 : pass
print(f"Deposited amount: ${atm.deposit(60)}") # You withdrew: $60 : pass
print(f"The funds you requested are {atm.check_withdraw(60)}") # The funds you requested are AVAILABLE : pass
print(f"Your account balance is: ${atm.withdraw(20)}") # Your account balance is 40 : pass
print(f"Deposited amount: ${atm.deposit(60)}") # You withdrew: $60 : pass
print(f"The funds you requested are {atm.check_withdraw(60)}") # The funds you requested are AVAILABLE : pass
print(f"Your account balance is: ${atm.withdraw(20)}") # Your account balance is 40 : pass
print(atm.print_transactions()) # Prints list line by line of each transaction
atm.enter_to_continue()