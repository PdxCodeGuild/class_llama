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

def pick6_nums_2():
    random_6 = []
    while len(random_6) < 6:
        n = randint(1,99)
        random_6.append(n)
    return random_6

# generate a list of 6 random numbers for winning numbers
def winning():
    winning = pick6_nums()
    return winning


# generate a list of 6 random numbers for the ticket
def ticket():
    ticket = pick6_nums()
    return ticket


# loop 100,000 times for each loop


# subtract 2 from balance (cost of ticket)
# def buy_ticket(balance):
#     balance = balance - 2
#     return balance

# find how many numbers match (value and position)
# def num_matches():
#     matches = 
#     return matches

# at the end of final loop print the final balance


# create main function
def main():
    # initialize balance at 0
    balance = 0
    balance = 22

    print(balance)


if __name__ == "__main__":
    main()