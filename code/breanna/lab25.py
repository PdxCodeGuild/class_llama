# ATM


class ATM:
    
    def __init__(self):
        self.balance = 0
        self.transactions = []
        
    def check_balance(self):
        print(f"${self.balance}")

    def deposit(self, deposit_amount):
        self.balance += int(deposit_amount)
        print(f"Your new balance is ${self.balance}.")
        self.transactions.append(f"user deposited ${deposit_amount}")

    def check_withdrawal(self, check_amount):
        if self.balance - int(check_amount) >= 0:
            print("You can withdraw this amount.")
            return True
        else:
            print("You can not withdraw this amount.")
            return False

    def withdraw(self, withdraw_amount):
        if self.check_withdrawal(check_amount) == True:
            self.balance -= int(withdraw_amount)
            print(f"Your new balance is ${self.balance}.")
            self.transactions.append(f"user withdrew ${withdraw_amount}")
        else:
            print("You cannot withdraw that amount.")

    def print_transactions(self):
        # maintain a running list of transactions ("user withdrew/deposited $x", etc.)
        print(self.transactions)

account = ATM()

while True:
    action = input("Would you like to check your balance (check b), make a deposit (deposit), check if an amount can be withdrawn (check w), make a withdrawal (withdraw), or check transactions (trans): ")
    if action == "check b":
            account.check_balance()
    elif action == "deposit":
            deposit_amount = input("How much would you like to deposit: $")
            account.deposit(deposit_amount)
    elif action == "check w":
            check_amount = input("How much would you like to withdraw: $")
            account.check_withdrawal(check_amount)
    elif action == "withdraw":
            withdraw_amount = input("How much would you like to withdraw: $")
            account.withdraw(withdraw_amount)
    elif action == "trans":
            account.print_transactions()