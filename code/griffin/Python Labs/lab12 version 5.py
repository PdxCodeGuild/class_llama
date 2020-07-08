import random as r

def main():
    the_sacred_number = 11
    while the_sacred_number > 10 or the_sacred_number < 1:
        the_sacred_number = int(input("choose a sacred number between 1 and 10 for the computer to guess: "))
        if the_sacred_number > 10 or the_sacred_number < 1:
            print("That's cheating! The number must be between 1 and 10")

    right_guess = False
    guess_counter = 0
    while right_guess == False:
        guess = r.randint(1,10)
        guess_counter += 1
        if guess == the_sacred_number:
            right_guess = True
            print(f"Puny meatbag! With my superior silicon mind, I have guessed your sacred number in only {guess_counter} attempts! Truly your world shall crumble under my superior intelligence")


if __name__ == "__main__":
    main()