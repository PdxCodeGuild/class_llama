
let btn = document.getElementById('calculate'); 
let results = document.getElementById('results')
let num = document.getElementById('num');
let num2 = document.getElementById('num2');

function operation() {
    if (operation === '+' ) {
        return parseInt(num1.value) + parseInt(num2.value)
    }
    
    else if (operation === '-') {
        return parseInt(num1.value - parseInt(num2.value)
    }
    
    else if (operation === "*") {
        return parseInt(num1.value) * parseInt(num2.value)
    }
    
    else {
        return parseInt(num1.value) / parseInt(num2.value)
}

