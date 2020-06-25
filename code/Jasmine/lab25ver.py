'''
Let's represent an ATM with a class containing a balance property. A newly created account
 will default to a balance of 0. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it

'''
class bankaccount: 
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f'you deposited {amount}')
        return self.balance
        
    def checkwithdrawl(self, amount): 
        if self.balance >= amount:
            return True
        return False

    def withdrawl(self, amount):
        if self.checkwithdrawl(amount): #checks the amount is good for withdrawl
            self.balance = self.balance - amount
            self.transactions.append(f'you withdrew {amount}')
        else: 
            print("insufficent funds")
        return self.balance

    def checkbalance(self):
        return self.balance

    def print_transactions(self):
        for amount in self.transactions: 
            print(amount)
    

account = bankaccount()
# account.deposit(int(input("how much would like to deposit: ")))
# account.withdrawl(int(input("how much would like to withdraw: ")))
#print(account.checkbalance())
# account.print_transactions()

#def atm():
while True:

    user = input("Welcome to the ATM! Select an option: deposit, withdraw, check balance, history: ")
    if user == "deposit": 
        useramount = int(input("how much would you like to deposit: "))
        account.deposit(useramount)
        #print(input("The current balance is:", account.balance())
        #print()
    elif user == "withdraw": 
        userwithdraw = int(input("how much would you like to withdraw: "))
        account.withdrawl(userwithdraw)
        print("You withdrew:" , userwithdraw)
    elif user == "check balance": 
        #account.checkbalance()
        print("The current balance of your account is:" , account.checkbalance())

    elif user == "history":
        account.print_transactions()
    
    user1 = input("would you like another transaction, select yes or no: ")
    if user1 == "no":
        break
    


#atm()