# Simple Calculator

def opening():
    print("Hey, let's MATH!!!")

def main():
    opening()

    num1 = int(input("What is the first number?"))
    num2 = int(input("What is the second number?"))

    text = input("Which operation would you like to use?")

    if text == "+":
        print("Addition, great!")
        print(f"{num1}{text}{num2}")

        sum = num1 + num2

        print(sum)
        return sum

    elif text == "-":
        print("Subtraction, great!")
        print(f"{num1}{text}{num2}")

        difference = num1 - num2

        print(difference)
        return difference

    elif text == "*":
        print("Multiplication, great!")
        print(f"{num1}{text}{num2}")

        product = num1 * num2

        print(product)
        return product

    elif text == "/":
        print("Division, great!")
        print(f"{num1}{text}{num2}")

        quotient = num1 / num2

        print(quotient)
        return quotient

    else:
        print("That is not math... See ya.")


main()