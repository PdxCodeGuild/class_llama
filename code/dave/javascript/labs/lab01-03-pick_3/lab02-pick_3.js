/*
This program is an ATM that allows: checks balance, deposit, check withdraw(amount) and withdraws(amount)
*/

// create the ATM class
let atm = {

    // initialization function
    init: function(this, balance){
        return this.balance = balance;
    },

    // Declare multiple functions for each actions
    
    // func that checks balance
    check_balance: function(this, balance){
        return this.balance;
    },

    // func that adds amount to balance
    deposit: function(this, amount){
        this.balance += amount;
        return this.balance;
    },
        
    // func that checks account balance
    check_withdrawl: function(this, amount){
        if (this.balance >= amount) {
            return console.log("AVAILABLE");
        }
        else {
            return console.log("NOT AVAILABLE");
        }
    },
        


    // func that withdraws the amount requested and returns it
    withdraw: function(this, amount){
        this.balance -= amount;
        return this.balance;
    }   
};


// let atm = console.log(Atm());
// console.log("Your balance is: ${atm.check_balance(0)}");
// console.log("Deposited amount: ${atm.deposit(60)}");
// console.log("The funds you requested are {atm.check_withdrawl(60)}");
// console.log("Your account balance is: ${atm.withdraw(20)}");
console.log("Your balance is: " + atm.check_balance());