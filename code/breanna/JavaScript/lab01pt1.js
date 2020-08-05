// JavaScript for Python Lab 11: Simple Calculator, Part 1
// You should first try to write them using JavaScript's prompt and alert in place of Python's input and print.

/* def math_prob():
    op = input("Which operation would you like to use? [+, -, *, /]")
    num1 = int(input("What is the first number?"))
    num2 = int(input("What is the second number?")) */

function math_prob() {
    let op = prompt("Which operation would you like to use? [+, -, *, /]")
    let num1 = Number(prompt("What is the first number?"))
    let num2 = Number(prompt("What is the second number?"))
    
    /* if op == "+":
        print("Addition, great!")
        print(f"{num1}{op}{num2}")
        sum = num1 + num2
        print(sum) */

    if (op === "+") {
        let sum = num1 + num2;
        alert(`Addition, great!\n${num1}${op}${num2}=${sum}`);
    }

    /* elif op == "-":
        print("Subtraction, great!")
        print(f"{num1}{op}{num2}")
        difference = num1 - num2
        print(difference) */
    
    else if (op === "-") {
        let difference = num1 - num2;
        alert(`Subtraction, great!\n${num1}${op}${num2}=${difference}`);
    }

    /* elif op == "*":
        print("Multiplication, great!")
        print(f"{num1}{op}{num2}")
        product = num1 * num2
        print(product) */

    else if (op === "*") {
        let product = num1 * num2;
        alert(`Multiplication, great!\n${num1}${op}${num2}=${product}`);
    }

    /* elif op == "/":
        print("Division, great!")
        print(f"{num1}{op}{num2}")
        quotient = num1 / num2
        print(quotient) */

    else if (op === "/") {
        let quotient = num1 / num2;
        alert(`Division, great!\n${num1}${op}${num2}=${quotient}`);
    }
}

/* while True:
    text = input("Would you like to solve a math problem? [yes/y, no/n]") */

while (true) {
    let text = prompt("Would you like to solve a math problem? [yes/y, no/n]")

    /* if text in ["yes", "y"]:
        math_prob() */

    if (["yes", "y"].includes(text)) {
        math_prob();
    }

    /* elif text in ["no", "n"]:
        print("Okay, goodbye.")
        break */

    else if (["no", "n"].includes(text)) {
        alert("Okay, goodbye.");
        break;
    }

    /* else:
        print("Please enter a valid response.") */
    
    else {
        alert("Please enter a valid response.")
    }

}