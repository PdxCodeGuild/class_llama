
let btn = document.getElementById('calculate'); 
let results = document.getElementById('results');
let ops = document.getElementById('operation');
let num = document.getElementById('num');
let num2 = document.getElementById('num2');

function operation() {
    if (ops.value === '+' ) {
        results.innerText = parseInt(num1.value) + parseInt(num2.value)
    }
    
    else if (ops.value === '-') {
        results.innerText =  parseInt(num1.value) - parseInt(num2.value)
    }
    
    else if (ops.value === "*") {
        results.innerText = parseInt(num1.value) * parseInt(num2.value)
    }
    
    else if (ops.value === "/") {
        results.innerText =  parseInt(num1.value) / parseInt(num2.value)
    }
}

    btn.addEventListener('click', operation)