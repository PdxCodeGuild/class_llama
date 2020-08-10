// JavaScript for Python Lab 11: Simple Calculator - Part 2

let solve = document.getElementById("solve")


solve.addEventListener("click", function(){
    
    let num1 = Number(document.getElementById("num1").value)
    let num2 = Number(document.getElementById("num2").value)
    let problemSolution = document.getElementById("problem-solution")

    let name = document.getElementById("solutionName")
    
    if (name !== null)
        name.innerText = ""
    
    let op = document.getElementsByName("op")
    let operator = ""

    for (let i = 0; i < op.length; i++) {
        if (op[i].checked) {
            operator += op[i].value;
        }
    }


    if (operator === "+") {
        let sum = num1 + num2;
        let solution = document.createElement("p");
        solution.setAttribute("id", "solutionName");
        solution.innerText = `${num1}${operator}${num2}=${sum}`;
        problemSolution.appendChild(solution);
    }
    else if (operator === "-") {
        let difference = num1 - num2;
        let solution = document.createElement("p");
        solution.setAttribute("id", "solutionName");
        solution.innerText = `${num1}${operator}${num2}=${difference}`;
        problemSolution.appendChild(solution);
    }
    else if (operator === "*") {
        let product = num1 * num2;
        let solution = document.createElement("p");
        solution.setAttribute("id", "solutionName");
        solution.innerText = `${num1}${operator}${num2}=${product}`;
        problemSolution.appendChild(solution);
    }
    else if (operator === "/") {
        let quotient = num1 / num2;
        let solution = document.createElement("p");
        solution.setAttribute("id", "solutionName");
        solution.innerText = `${num1}${operator}${num2}=${quotient}`;
        problemSolution.appendChild(solution);
    }
})