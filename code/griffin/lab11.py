
def add(num1, num2):
    answer = num1 + num2
    return answer

def subtract(num1, num2):
    answer = num1 - num2
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def divide(num1, num2):
    answer = num1 / num2
    return answer


def main():
    while True:
        operator = input("Which operator would you like to use? Enter +, -, *, or /, or type 'done' to quit. ")
        if operator == "done":
            break
        else:
            first_number = int(input("what is the first number? "))
            second_number = int(input("What is the second number? "))
            if operator == "+":
                answer = add(first_number, second_number)
            elif operator == "-":
                answer = subtract(first_number, second_number)
            elif operator == "*":
                answer = multiply(first_number, second_number)
            elif operator == "/":
                answer = divide(first_number, second_number)
            print(f"{first_number} {operator} {second_number} = {answer}")





if __name__ == "__main__":
    main()