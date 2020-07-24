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

## TESTS FOR Atm Class
# print(f"You're balance is: ${atm.check_balance(0)}") # 0 : pass
# print(f"Deposited amount: ${atm.deposit(60)}") # You withdrew: $60 : pass
# print(f"The funds you requested are {atm.check_withdrawl(60)}") # The funds you requested are AVAILABLE : pass
# print(f"Your account balance is: ${atm.withdraw(20)}") # Your account balance is 40 : pass
# print(atm.print_transactions()) # You 

if __name__ == "__main__":

    # clear terminal screen when program is run
    atm.clear()

    # while loop that keeps returning to MENU until user enters (Q) to quit
    while True:
        print()
        print("******************* GlobUS Bank ********************")
        print("****************************************************")
        print()
        print("(D): Deposit")
        print("(W): Withdraw")
        print("(C): Check if requested funds are available")
        print("(H): History")
        print("(Q): Quit")
        print()

        # convert the 'choice' variable to lower case when the user enters their input
        choice = input("Welcome, Please select (D), (W), (C), (H), or (Q): ").lower()

        # if statements to run code based on user input from 'choices'
        if choice == 'd':
            print()

            # while loop that asks user to input a number and handles ValueError if int is not input
            while True:
                try:
                    amount = int(input("How much would you like to deposit (enter a number): $"))
                    break
                except ValueError:
                    input("Sorry, you entered an amount other than a number. Press (ENTER) to try again. ")
                
            deposited = atm.deposit(amount)
            print(f"You're balance is ${deposited}")
            atm.enter_to_continue()
            

        elif choice == 'w':
            print()

            # while loop that asks user to input a number and handles ValueError if int is not input
            while True:
                try:
                    amount = int(input("How much would you like to withdraw (enter a number): $"))
                    break
                except ValueError:
                    input("Sorry, you entered an amount other than a number. Press (ENTER) to try again. ")
            withdrawn = atm.withdraw(amount)
            print(f"You're balance is ${withdrawn} ")
            atm.enter_to_continue()

        elif choice == 'c':
            print()
            amount = int(input("How much would you like to withdraw: $"))
            funds = atm.check_withdraw(amount)
            print(f"The funds you requested are: {funds}")
            atm.enter_to_continue()

        elif choice == 'h':
            print()
            history = atm.print_transactions()
            print(history)
            atm.enter_to_continue()
            

        elif choice == 'q':
            atm.clear()
            break
        else:
            print()
            print()
            input("Whoops, you didn't enter a valid input. Press (ANY) key to continue. ")
            atm.clear()
        
