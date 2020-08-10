let cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"J":10,"Q":10,"K":10};
let key_card = Object.keys(cards);
let total_value = 0;

function card_check(n) {
    if (n == key_card[n]) {
        total_value += cards[key_card[n]];
        alert(cards[key_card[n]])
        return total_value;


let bt = document.getElementById("bt");

bt.addEventListener('click', function() {
    let cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10};
    let key_card = Object.keys(cards);
    let total_value = 0;
    let card_id = 0
    for (let i = 0; i<3; i++) {
        card_id = Math.round(12*Math.random());
        card_value = cards[Object.keys(cards)[card_id]];
        total_value += card_value;
        alert(total_value);

    }
}

for (let i = 0; i<3; i++) {
    let card_id = Math.round(11*Math.random());
    key_card.forEach(card_check);

}

if (total_value < 17) {
    alert("I advise: hit!")
}   else if (17 < total_value < 21) {
    alert("I advise: stay!")
}   else if (total_value == 21) {
    alert("Blackjack!")
}   else {
    alert("Ya busted")
}

alert(total_value)

    if (total_value > 21) {
        alert("Ya busted");
    }   else if (total_value == 21) {
        alert("Blackjack!");
    }   else if (17 < total_value < 21) {
        alert("I advise: stay!");
    }   else {
        alert("I advise: hit!")
    };
});