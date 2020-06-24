class Account:
    def __init__(self,balance=0):
        self.balance = balance

    def check_balance(self):
        print(f'Your account contains ${self.balance}')

    def deposit(self):
        dep = int(input("How much is deposited? "))
        self.balance+= dep

    def withdraw(self):
        withdraw = int(input("How much would you like to withdraw? "))
        self.balance -= withdraw

    def check_withdrawal(self,amount):
        if self.balance >= amount:
            return True
        else:            
            return False
            

checking = Account(500)
checking.check_withdrawal(600)
checking.check_balance()