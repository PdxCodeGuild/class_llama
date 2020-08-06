// JavaScript for Python Lab 25: ATM - Part 1

// class ATM:

class ATM {
    
    /* def __init__(self):
        self.balance = 0
        self.transactions = [] */

    constructor(balance) {
        this.balance = 0;
        this.transactions = [];
    }
        
    /* def check_balance(self):
        print(f"${self.balance}") */

    check_balance() {
        alert(`Current balance: $${this.balance}`);
    }

   /* def deposit(self, deposit_amount):
        self.balance += int(deposit_amount)
        print(f"Your new balance is ${self.balance}.")
        self.transactions.append(f"user deposited ${deposit_amount}") */

    deposit(deposit_amount) {
        this.balance += Number(deposit_amount);
        alert(`New balance: $${this.balance}`);
        this.transactions.push(`Deposited: $${deposit_amount}`);
    }

    /* def check_withdrawal(self, check_amount):
        if self.balance - int(check_amount) >= 0:
            print("You can withdraw this amount.")
            return True
        else:
            print("You can not withdraw this amount.")
            return False */

    check_withdrawal(check_amount) {
        if (this.balance - Number(check_amount) >= 0) {
            return true;
        }
        else {
            alert("You cannot withdraw this amount.");
            return false;
        }
    }

    /* def withdraw(self, withdraw_amount):
        if self.check_withdrawal(check_amount) == True:
            self.balance -= int(withdraw_amount)
            print(f"Your new balance is ${self.balance}.")
            self.transactions.append(f"user withdrew ${withdraw_amount}")
        else:
            print("You cannot withdraw that amount.") */

    withdraw(withdraw_amount) {
        if (this.check_withdrawal(withdraw_amount) === true) {
            this.balance -= Number(withdraw_amount);
            alert(`New balance: $${this.balance}`);
            this.transactions.push(`Withdrew: $${withdraw_amount}`);
        }
        else {
            alert("You cannot withdraw this amount.");
        }
    }

    /* def print_transactions(self):
        # maintain a running list of transactions ("user withdrew/deposited $x", etc.)
        print(self.transactions) */

    print_transactions() {
        alert(`${this.transactions}`);
    }
}

// account = ATM()

let account = new ATM()

/* while True:
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
            account.print_transactions() */
  
while (true) {
    let action = prompt("Please make a selection: \ncheck current balance (check b) \nmake a deposit (deposit) \ncheck if an amount can be withdrawn (check w) \nmake a withdrawal (withdraw) \ncheck transactions (trans) \n\nSelection: ")

    if ("check b".includes(action)) {
        account.check_balance();
    }
    else if ("deposit".includes(action)) {
        let deposit_amount = prompt("Deposit amount: $");
        account.deposit(deposit_amount);
    }
    else if ("check w".includes(action)) {
        let check_amount = prompt("Check withdrawal amount: $");
        account.check_withdrawal(check_amount);
    }
    else if ("withdraw".includes(action)) {
        let withdraw_amount = prompt("Withdrawal amount: $");
        account.withdraw(withdraw_amount);
    }
    else if ("trans".includes(action)) {
        account.print_transactions();
    }
    else {
        alert("Please make a valid selection - check b, deposit, check w, withdraw, or trans");
    }
}