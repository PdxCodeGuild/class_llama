/*
This program is an ATM that allows: checks balance, deposit, check withdraw(amount) and withdraws(amount)
*/


// create the ATM class
class Atm {

    constructor() {
        this.balance = 0;
        return this.balance;
    }

    // Declare multiple functions for each actions
    
    // func that checks balance
    check_balance() {
        return this.balance;
    }

    // func that adds amount to balance
    deposit(amount) {
        this.balance += amount;
        return this.balance;
    }
        
    // func that checks account balance
    check_withdrawl(amount) {
        if (this.balance >= amount) {
            return console.log("AVAILABLE");
        }
        else {
            return console.log("NOT AVAILABLE");
        }
    }

    // func that withdraws the amount requested and returns it
    withdraw(amount) {
        this.balance -= amount;
        return this.balance;
    }
}   

let customer1;
customer1 = new Atm();

console.log(customer1.check_balance());
console.log(customer1.deposit(5));
console.log(customer1.check_balance());


