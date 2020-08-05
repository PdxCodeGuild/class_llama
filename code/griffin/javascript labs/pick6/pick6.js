
function pick6() {
    let chosen_numbers = [];
    for (let i=0; i<6; i++) {
        chosen_numbers.push(Math.round(100*Math.random()))
    };
    return chosen_numbers;
};

function num_matches(winning, ticket) {
    let wincounter = 0;
    let winnings = 0;
    for (let i=0; i<6; i++) {
        if (winning[i] == ticket[i]) {
            wincounter++
        };
    };
    
    if (wincounter == 0) {
        winnings = 0;
    } else if (wincounter == 1) {
        winnings = 4;
    } else if (wincounter == 2) {
        winnings = 7;
    } else if (wincounter == 1) {
        winnings = 100;
    } else if (wincounter == 1) {
        winnings = 50000;
    } else if (wincounter == 1) {
        winnings = 1000000;
    } else if (wincounter == 1) {
        winnings = 25000000;
    };

    return winnings;

}

function main() {
    let play_number = parseInt(prompt("How many times do you want to play the lottery? "));
    let savings_account = 0;
    let earnings = 0;
    let expenses = 0;
    let ticket = [];
    let winning = [];
    let money_won = 0;

    for (let i=0; i< play_number;i++) {
        ticket = pick6();
        winning = pick6();
        money_won = num_matches(winning, ticket);
        expenses += 2;
        earnings += money_won;
        console.log(i, money_won);
    };

    savings_account = earnings - expenses;
    roi = (savings_account/expenses)*100

    alert(`You spent $${expenses} on lottery tickets, and won $${earnings}. Your return on investment is ${roi}%... you dumb idiot`);

}

main();
