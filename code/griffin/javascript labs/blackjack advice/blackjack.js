

let bt = document.getElementById("bt");

bt.addEventListener('click', function() {
    let cards = {"Ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10};
    let key_card = Object.keys(cards);
    let total_value = 0;
    let card_id = 0;

    
    card_id = Math.round(12*Math.random());
    selected_card = Object.keys(cards)[card_id];
    card_value = cards[Object.keys(cards)[card_id]];
    total_value += card_value;
    let card1 = document.getElementById("card1");
    card1.innerText = `First Card: ${selected_card}`

    card_id = Math.round(12*Math.random());
    selected_card = Object.keys(cards)[card_id];
    card_value = cards[Object.keys(cards)[card_id]];
    total_value += card_value;
    let card2 = document.getElementById("card2");
    card2.innerText = `Second Card: ${selected_card}`;

    card_id = Math.round(12*Math.random());
    selected_card = Object.keys(cards)[card_id];
    card_value = cards[Object.keys(cards)[card_id]];
    total_value += card_value;
    let card3 = document.getElementById("card3");
    card3.innerText = `Third Card: ${selected_card}`;
        
    let advice = document.getElementById("advice");

    if (total_value > 21) {
        advice.innerText = `Total Value: ${total_value}. Ya busted`;
    }   else if (total_value == 21) {
        advice.innerText = `Total Value: ${total_value}. Blackjack!`;
    }   else if (17 < total_value < 21) {
        advice.innerText = `Total Value: ${total_value}. I advise: stay!`;
    }   else {
        advice.innerText = `Total Value: ${total_value}. I advise: hit!`;
    };
});











