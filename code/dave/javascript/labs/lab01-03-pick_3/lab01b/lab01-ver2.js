/*
This program gives basic blackjack advice during a game by asking for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.
*/

// store values for cards in a dictionary
var card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10};



// initailize variables
let card_sum = 0

function main(){

    

//     /*  
//     prompt user for 3 cards create while loop that asks
//     for user card prompt. if not valid it will keep
//     prompting until correct value is prompt
//     */
//     let first_card = prompt("What's your first card? ").toUpperCase();
//     while (!(first_card in card_values)) {
//         first_card = prompt("Not a valid card, enter another card value for first card: ").toUpperCase();
//     }
//     console.log(first_card);


//     let second_card = prompt("What's your second card? ").toUpperCase();
//     while (!(second_card in card_values)){
//         second_card = prompt("Not a valid card, enter another card value for second card: ").toUpperCase();
//     }
//     console.log(second_card)


//     let third_card = prompt("What's your third card? ").toUpperCase();
//     while (!(third_card in card_values)){
//         third_card = prompt("Not a valid card, enter another card value for third card: ").toUpperCase();
//     }
//     console.log(third_card);

    let first_card = document.getElementById("num1").value;
    let second_card = document.getElementById("num2").value;
    let third_card = document.getElementById('num3').value;

    first_card = card_values[first_card];
    second_card = card_values[second_card];
    third_card = card_values[third_card];


    let card_sum = first_card + second_card + third_card;

    if (card_sum < 17) {
        document.getElementById('advice').innerHTML = 'Hit';
    }
    else if (card_sum > 17 && card_sum < 21) {
        document.getElementById('advice').innerHTML = 'Stay';
    }
    else if (card_sum == 21) {
        document.getElementById('advice').innerHTML = 'Blackjack!!';
    }    
    else {
        document.getElementById('advice').innerHTML = 'Already Busted';
    }
}

console.log(main());