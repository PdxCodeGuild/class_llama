# Simple Calculator

def math_prob():

    text = input("Which operation would you like to use? [+, -, *, /]")

    num1 = int(input("What is the first number?"))
    num2 = int(input("What is the second number?"))

    if text == "+":
        print("Addition, great!")
        print(f"{num1}{text}{num2}")

        sum = num1 + num2

        print(sum)

    elif text == "-":
        print("Subtraction, great!")
        print(f"{num1}{text}{num2}")

        difference = num1 - num2

        print(difference)

    elif text == "*":
        print("Multiplication, great!")
        print(f"{num1}{text}{num2}")

        product = num1 * num2

        print(product)

    elif text == "/":
        print("Division, great!")

        quotient = num1 / num2

        print(f"{num1}{text}{num2}")
        print(quotient)



while True:

    text = input("Would you like to solve a math problem? [yes/y, no/n]")

    if text in ["yes", "y"]:
        math_prob()
    
    elif text in ["no", "n"]:
        print("Okay, goodbye.")
        break

    else:
        print("Please enter a valid response.")
        
