'''

Lab 25: ATM
Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
Version 2
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.

Version 3
Allow the user to enter commands into a REPL.

> what would you like to do (deposit, withdraw, check balance, history)?
> deposit
> how much would you like to deposit?
> $5
> what would you like to do (deposit, withdraw, check balance, history)?
> check balance
> balance: $5

'''

class Atm:

  def __init__(self,balance= 0):
    self.balance = balance
    self.history = []
  def check_balance(self):
    print(f'your balance is {self.balance}')

  def check_withdrawal(self, check_withdrawal):
    if self.balance <= check_withdrawal:
      return False
    if self.balance >= check_withdrawal:
      return True

  def deposit(self, deposit):
    self.balance += deposit
    print(f'Your balance is now {self.balance}')
    self.history.append(f'User deposited {deposit}')
  def withdraw(self, withdraw):
    if self.check_withdrawal(withdraw) == True: 
      self.balance -= withdraw
      print(f'Your balance is now {self.balance}')
      self.history.append(f'User withdrew {withdraw}')
    else:
      print('Your lack of funds disturbs me')
      self.history.append("User attempted to overdraft")
      
    
  def check_history(self):
      for i in self.history:
        print(i)
  



balance = Atm(0)
# balance.check_balance()

while True:

  user_input = input('Would you like to deposit, withdraw, check balance, or bank statement?: ')

  if user_input == 'deposit':
    user_deposit = int(input('How much would you like to deposit?: '))
    balance.deposit(user_deposit)
  elif user_input == 'check balance':
    balance.check_balance()
  elif user_input == 'withdraw':
    user_withdraw = int(input('How much would you like to withdraw?: '))
    balance.withdraw(user_withdraw)
  elif user_input == 'bank statement':
    balance.check_history()

        








