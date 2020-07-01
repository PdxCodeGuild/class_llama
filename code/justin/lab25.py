class Machine:
        
    def __init__(self):
        self.balance = 0
        self.transactions = []
        
    def check_balance(self):
        self.transactions.append(f"User checked balance of ${self.balance}.")
        return self.balance

    def deposit(self, amount):
        self.transactions.append(f"User deposited ${amount}.")
        self.balance += amount
        
    def withdrawl(self, amount):
        self.transactions.append(f"User withdrew ${amount}.")
        self.balance -= amount

    def check_withdrawl(self, amount):
        return self.balance >= amount

    def trans_list(self):
        for action in self.transactions:
            print(action)

atm = Machine()

def atm_ui():
    print("Welcome to the ATM!")
    
    while True:
        print("\n" "What transaction would you like to perform?" "\n" "Type the number or letter from the following options:" "\n")
        print("-> (D)eposit [1]")
        print("-> (W)ithdrawl [2]")
        print("-> Check (B)alance [3]")
        print("-> Transaction (H)istory [4]")
        print("-> (E)xit [5]" "\n")
        action = input("Your selection: ").lower().strip()
        print("")
        
        valid_actions = ['1', '2', '3', '4', '5', 'd', 'w', 'b', 'h', 'e', 
        'deposit', 'withdrawl', 'check balance', 'transaction history', 'exit']
       
        if action in valid_actions:
            
            # Deposit
            if action in ['1', 'd', 'deposit']:
                # using a float for the amount gives the option for cents
                amount = int(input("How much would you like to deposit?: ").strip("$"))
                atm.deposit(amount)
                print(f"You have deposited ${amount}, your new balance is ${atm.check_balance()}.")

            # Withdrawl
            elif action in ['2', 'w', 'withdrawl']:
                amount = int(input("How much would you like to withdraw?: ").strip("$"))
                if atm.check_withdrawl(amount) == True:
                    atm.withdrawl(amount)
                    print(f"You have withdrawn ${amount}, your new balance is ${atm.check_balance()}.")
                else:
                    print(f"Insufficient funds. You only have a balance of ${atm.check_balance()}.")
                    
            # Check Balance
            elif action in ['3', 'b', 'check balance']:
                print(f"Your balance is ${atm.check_balance()}.")
                                
            # Check Transactions
            elif action in ['4', 'h', 'transaction history']:
                print("The following transactions were made:")
                atm.trans_list()
            
            # Exit
            elif action in ['5', 'e', 'exit']:
                print("Thank you, have a great day!")
                return False
       
        elif action not in valid_actions:
            print("ERROR: Invalid entry, please try again.")
        
atm_ui()