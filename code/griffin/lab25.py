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
            
def main():
    checking = Account()
    while True:
        choice = int(input("""Please choose from among the following options:

        (1) Deposit
        (2) Withdrawal
        (3) Check Balance
        (4) Clear Check
        (5) Transaction History
        (6) Log Off
        """))
        if choice == 1:
            checking.deposit()
        elif choice == 2:
            checking.withdraw()
        elif choice == 3:
            checking.check_balance()
        elif choice == 4:
            check_amount = int(input("How much is this check for? "))
            status = checking.check_withdrawal(check_amount)
            if status == True:
                print("That check will clear")
            else:
                print("That check will not clear")
        elif choice == 5:
            checking.print_transactions()
        elif choice == 6:
            break

if __name__ == "__main__":
    main()