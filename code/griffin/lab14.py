import random as r

def pick6():
    chosen_numbers = []
    while len(chosen_numbers) < 6:
        new_num = r.randint(1,100)
        chosen_numbers.append(new_num)
    return chosen_numbers

def num_matches(winning, ticket):
    wincounter = 0
    for i, value in enumerate(ticket):
        if value == winning[i]:
            wincounter += 1
    if wincounter == 0:
        winnings = 0
    elif wincounter == 1:
        winnings = 4
    elif wincounter == 2:
        winnings = 7
    elif wincounter == 3:
        winnings = 100
    elif wincounter == 4:
        winnings = 50000
    elif wincounter == 5:
        winnings = 1000000
    elif wincounter == 6:
        winnings = 25000000
    return winnings

def main():
    savings_account = 0
    purchase_counter = 0
    earnings = 0
    expenses = 0

    while purchase_counter < 100000:
        savings_account = savings_account - 2
        expenses = expenses + 2
        winning = pick6()
        ticket = pick6()
        prizes = num_matches(winning, ticket)
        savings_account = savings_account + prizes
        earnings = earnings + prizes
        purchase_counter += 1

    return_on_investment = 100 * (earnings - expenses)/expenses
    print(f"you have earned a total of ${savings_account}")
    print(f"your return on investment is {return_on_investment}%")
    
if __name__ == "__main__":
    main()