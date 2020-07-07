import random as r 

def main():
    print("Welcome to the number guesser. The number is between 1 and 10. Try to guess it, or die.")
    num = r.randint(1,10)
    right_guess = False
    guess_counter = 0
    last_guess = 0
    while right_guess == False:
        guess = int(input("\nWhat do you think the number is? "))
        guess_counter += 1
        if guess == num:
            print("You got it!")
            right_guess = True
            print(f"You used {guess_counter} guesses")
        elif guess_counter == 10:
            print("You guessed 10 times. You lose.")
            right_guess = True
        else:
            if guess > num:
                print("try lower")
            elif guess < num:
                print("try higher")
            if last_guess > 0:
                if abs(guess - num) < abs(last_guess - num):
                    print("warmer...")
                else:
                    print("colder...")
        last_guess = guess


if __name__ == "__main__":
    main()