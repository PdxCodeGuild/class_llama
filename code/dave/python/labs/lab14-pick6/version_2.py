"""
# Lab 14: Pick6

Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'.
Then try playing pick6 100,000 times, with the ticket cost and payoff
below.
"""
from random import randint

# create function that generates a list of 6 random numbers
def pick6_nums():
    random_6 = []
    for i in range(0,6):
        n = randint(1,99)
        random_6.append(n)
    return random_6

# subtract 2 from balance (cost of ticket)

# create main function
def main():

    ### VARIABLES
    # initialize balance
    balance = 0

    # loop through 100,000 times
    for i in range(0,100000):
        
        balance -= 2
        # generate a list of 6 random numbers for the ticket
        ticket = pick6_nums()
        # generate a list of 6 random numbers for winning numbers
        winning = pick6_nums()

        # compare ticket to winning numbers
        match = list(zip(ticket,winning))
        count = 0
        for ticket,winning in match:
            if ticket == winning:
                count += 1
            else:
                pass
        print(count)

        if count == 1:
            print("you win $4")
            balance += 4
        if count == 2:
            print("you win $7")
            balance += 7
        if count == 3:
            print("you win $100")
            balance += 100
        if count == 4:
            print("you win $50,000")
            balance += 50000
        if count == 5:
            print("you win $1,000,000")
            balance += 1000000
        if count == 6:
            print("you win $25,000,000")
            balance += 25000000

    balance_converted = str(balance)
    print("Your final balance is $" + balance_converted)

    roi = balance / 200000
    roi_converted = str(roi)
    print("Your ROI (return on investment) is $" + roi_converted)

    # at the end of final loop print the final balance


if __name__ == "__main__":
    main()