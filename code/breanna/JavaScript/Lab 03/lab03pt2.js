// JavaScript for Python Lab 25: ATM - Part 2

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
        } else {
            return false;
        }
    }

    withdraw(withdraw_amount) {
        if (this.check_withdrawal(withdraw_amount) === true) {
            this.balance -= Number(withdraw_amount);
            this.transactions.push(`Withdrew: $${withdraw_amount}`);
        } else {
            alert("You cannot withdraw this amount.");
        }
    }

    print_transactions() {
        return this.transactions;
    }
}

let account = new ATM()

let depositAmount = document.getElementById("deposit-amount-s")
depositAmount.addEventListener("click", function(){
    account.deposit(document.getElementById("deposit-amount").value);
    document.getElementById("deposit-amount").value = "";
    document.getElementById("current-balance").innerText = account.check_balance();
    let showTrans = document.getElementById("all-transactions");
    showTrans.innerHTML = "";
    account.print_transactions().forEach(function(transaction) {
        let li = document.createElement("li");
        li.innerText = transaction;
        li.addEventListener("click", function() {
            alert(this.innerText);
        });
        showTrans.append(li);
    })
})

let withdrawAmount = document.getElementById("withdrawal-amount-s")
withdrawAmount.addEventListener("click", function() {
    account.withdraw(document.getElementById("withdrawal-amount").value);
    document.getElementById("withdrawal-amount").value = "";
    document.getElementById("current-balance").innerText = account.check_balance();
    let showTrans = document.getElementById("all-transactions");
    showTrans.innerHTML = "";
    account.print_transactions().forEach(function(transaction) {
        let li = document.createElement("li");
        li.innerText = transaction;
        li.addEventListener("click", function() {
            alert(this.innerText);
        });
        showTrans.append(li);
    })
})

withdrawal = document.getElementById("withdrawal-amount")
withdrawal.addEventListener("input", function() {
    if (account.check_withdrawal(this.value)) {
        withdrawAmount.removeAttribute("disabled");
    } else {
        withdrawAmount.setAttribute("disabled", "true");
    }
});

let reset = document.getElementById("reset")
reset.addEventListener("click", function() {
    account = new ATM()
    document.getElementById("current-balance").innerText = account.check_balance();
    let showTrans = document.getElementById("all-transactions");
    showTrans.innerHTML = "";
    account.print_transactions().forEach(function(transaction) {
        let li = document.createElement("li");
        li.innerText = transaction;
        li.addEventListener("click", function() {
            alert(this.innerText);
        });
        showTrans.append(li);
    })
})