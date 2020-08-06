

alert("Welcome to the basic calculator")

let number = parseInt(prompt("what is your first number: "))
alert("your first number is " + number)
console.log(number)

let operation = prompt("what operation would you like to use (+, -, * , /)?")
alert("You picked: " + operation)
console.log(operation)

let second = parseInt(prompt("what is your second number: "))
alert("your second number is: " + second)
console.log(second)

alert("Your equation is: " + number + operation + second)

if (operation === '+' ) {
    alert(number + second)
}

else if (operation === '-') {
    alert(number - second)
}

else if (operation === "*") {
    alert(number * second)
}

else {
    alert(number / second)
}