/*
This program is an ATM that allows: checks balance, deposit, check withdraw(amount) and withdraws(amount)
*/


// create the ATM class
class Atm {

    constructor(balance=0) {
        this.balance = balance;
    }

    // Declare multiple functions for each actions
    
    // func that checks balance
    check_balance() {
        return this.balance;
    }

    // func that adds amount to balance
    deposit(amount) {
        this.balance += amount;
        document.getElementById('result').innerHTML = 'You deposited ' + amount + '.' + 'Your new balance is' + this.balance + '.';
    }
        
    // func that checks account balance
    check_withdrawl(amount) {
        return this.balance >= amount;
    }

    // func that withdraws the amount requested and returns it
    withdraw(amount) {
        this.balance -= amount;
        document.getElementById('result').innerHTML = 'You withdrew ' + amount + '. ' + 'Your new balance is' + this.balance + '.';
    }

}   


let check_balance = document.getElementById("check-balance");
let deposit = document.getElementById("deposit");
let withdraw = document.getElementById("withdraw");

check_balance.addEventListener("click", function() {
    customer = new Atm;
    balance = customer.check_balance;
    console.log(balance);
    document.getElementById("result").innerHTML = 'Your balance is ' + balance;
});


