class Account:

    def __init__(self,balance=0,transaction_record = []):
        self.balance = balance
        self.transaction_record = transaction_record


    def check_balance(self):
        print(f'Your account contains ${self.balance}')

    def deposit(self):
        dep = int(input("How much is deposited? "))
        self.balance+= dep
        self.transaction_record.append(f"you deposited ${dep}")

    def withdraw(self):
        withdraw = int(input("How much would you like to withdraw? "))
        self.balance -= withdraw
        self.transaction_record.append(f"you withdrew ${withdraw}")

    def check_withdrawal(self,amount):
        if self.balance >= amount:
            return True
        else:            
            return False

    def print_transactions(self):
        print(self.transaction_record)
            

checking = Account(500)
checking.deposit()
checking.withdraw()
checking.print_transactions()