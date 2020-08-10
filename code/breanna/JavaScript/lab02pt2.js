// JavaScript for Python Lab 19: Blackjack Advice - Part 2

let advice = document.getElementById("advice")

advice.addEventListener("click", function(){

    let f_card = document.getElementById("fcard").value
    let s_card = document.getElementById("scard").value
    let t_card = document.getElementById("tcard").value
    let blackjackAdvice = document.getElementById("blackjack-advice")

    if (blackjackAdvice !== null)
        blackjackAdvice.innerHTML = ""

    if (["J","j","Q","q","K","k"].includes(f_card)) {
        f_card = 10
        console.log(f_card, "first face card")
    }
    else if (["A","a"].includes(f_card)) {
        f_card = 1
        console.log(f_card, "first ace")
    }
    else {
        f_card = Number(f_card)
        console.log(f_card, "first number")
    }

    if (["J","j","Q","q","K","k"].includes(s_card)) {
        s_card = 10
        console.log(s_card, "second face card")
    }
    else if (["A","a"].includes(s_card)) {
        s_card = 1
        console.log(s_card, "second ace")
    }
    else {
        s_card = Number(s_card)
        console.log(s_card, "second number")
    }

    if (["J","j","Q","q","K","k"].includes(t_card)) {
        t_card = 10
        console.log(t_card, "third face card")
    }
    else if (["A","a"].includes(t_card)) {
        t_card = 1
        console.log(t_card, "third ace")
    }
    else {
        t_card = Number(t_card)
        console.log(t_card, "third number")
    }

    let total = f_card + s_card + t_card

    if (total == 21) {
        let advice = document.createElement("p");
        advice.setAttribute("id", "adviceName");
        advice.innerText = `${total} - Blackjack!`;
        blackjackAdvice.appendChild(advice);
    }
    else if (total > 21) {
        let advice = document.createElement("p");
        advice.setAttribute("id", "adviceName");
        advice.innerText = `${total} - bust`;
        blackjackAdvice.appendChild(advice);
    }
    else if (total < 21 && total >= 17) {
        let advice = document.createElement("p");
        advice.setAttribute("id", "adviceName");
        advice.innerText = `${total} - stay`;
        blackjackAdvice.appendChild(advice);
    }
    else if (total < 17) {
        let advice = document.createElement("p");
        advice.setAttribute("id", "adviceName");
        advice.innerText = `${total} - hit`;
        blackjackAdvice.appendChild(advice);
    }
})