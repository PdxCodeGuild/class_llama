def main():
    while True:
        equation = input("Please enter an equation or type 'done' to quit: ")
        if equation == "done":
            break
        else:
            answer = eval(equation)
            print(answer)

if __name__ == "__main__":
    main()