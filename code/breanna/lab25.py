# ATM


class ATM:
    
    def __init__(self):
        self.balance = 0
        self.transactions = []
        
    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += deposit_amount

    def check_withdrawal(self, amount):
        if self.balance - check_amount <= 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.check_withdrawal() == True:
            self.balance -+ withdraw_amount
            print(f"Your new balance is ${self.balance}.")
        else:
            print("You cannot withdraw that amount.")

    def print_transactions(self):
        self.transactions.append()