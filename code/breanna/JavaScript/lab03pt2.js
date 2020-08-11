// JavaScript for Python Lab 25: ATM - Part 2

// is this even necessary? automatically updates/shows, no need for button?
let option1 = document.getElementById("option1")
option1.addEventListener("click", function(){
    document.getElementById("check-balance").innerText = `Current balance: ${account.check_balance()}`;
})

let option2 = document.getElementById("option2")
option2.addEventListener("click", function(){
    let deposit = document.getElementById("deposit")
    if (deposit.style.display === "block") {
        deposit.style.display = "none"
    } else {
        deposit.style.display = "block"
    }
})

let depositAmount = document.getElementById("deposit-amount-s")
depositAmount.addEventListener("click", function(){
    account.deposit(document.getElementById("deposit-amount").value);
    document.getElementById("check-balance").innerText = `Current balance: ${account.check_balance()}`;
})

let option3 = document.getElementById("option3")
option3.addEventListener("click", function(){
    let checkWithdrawal = document.getElementById("check-withdrawal")
    if (checkWithdrawal.style.display === "block") {
        checkWithdrawal.style.display = "none"
    } else {
        checkWithdrawal.style.display = "block"
    }
})

let withdrawAmountC = document.getElementById("check-withdrawal-amount-s")
withdrawAmountC.addEventListener("click", function(){
    account.check_withdrawal(document.getElementById("check-withdrawal-amount").value);
    document.getElementById("check-balance").innerText = `Current balance: ${account.check_balance()}`;
    // if statement for true/false below to show if amount can be withdrawn? keep alerts? show would-be balance?
})

let option4 = document.getElementById("option4")
option4.addEventListener("click", function(){
    let withdraw = document.getElementById("withdrawal")
    if (withdraw.style.display === "block") {
        withdraw.style.display = "none"
    } else {
        withdraw.style.display = "block"
    }
})

let withdrawAmount = document.getElementById("withdrawal-amount-s")
withdrawAmount.addEventListener("click", function() {
    account.withdraw(document.getElementById("withdrawal-amount").value);
    document.getElementById("check-balance").innerText = `Current balance: ${account.check_balance()}`;
})

let option5 = document.getElementById("option5")
option5.addEventListener("click", function(){
    
})

class ATM {
    
    constructor(balance) {
        this.balance = 0;
        this.transactions = [];
    }
     
    check_balance() {
        return this.balance;
    }

    deposit(deposit_amount) {
        this.balance += Number(deposit_amount);
        this.transactions.push(`Deposited: $${deposit_amount}`);
    }

    check_withdrawal(check_amount) {
        if (this.balance - Number(check_amount) >= 0) {
            return true;
        }
        else {
            alert("You cannot withdraw this amount.");
            return false;
        }
    }

    withdraw(withdraw_amount) {
        if (this.check_withdrawal(withdraw_amount) === true) {
            this.balance -= Number(withdraw_amount);
            this.transactions.push(`Withdrew: $${withdraw_amount}`);
        }
        else {
            alert("You cannot withdraw this amount.");
        }
    }

    print_transactions() {
        return this.transactions;
    }
}

let account = new ATM()

// while (true) {
//     let action = prompt("Please make a selection: \ncheck current balance (check b) \nmake a deposit (deposit) \ncheck if an amount can be withdrawn (check w) \nmake a withdrawal (withdraw) \ncheck transactions (trans) \nquit \n\nSelection: ")

//     if ("check b".includes(action)) {
//         account.check_balance();
//     }
//     else if ("deposit".includes(action)) {
//         let deposit_amount = prompt("Deposit amount: $");
//         account.deposit(deposit_amount);
//     }
//     else if ("check w".includes(action)) {
//         let check_amount = prompt("Check withdrawal amount: $");
//         account.check_withdrawal(check_amount);
//     }
//     else if ("withdraw".includes(action)) {
//         let withdraw_amount = prompt("Withdrawal amount: $");
//         account.withdraw(withdraw_amount);
//     }
//     else if ("trans".includes(action)) {
//         account.print_transactions();
//     }
//     else if ("quit".includes(action)) {
//         break;
//     }
//     else {
//         alert("Please make a valid selection - check b, deposit, check w, withdraw, or trans");
//     }
// }