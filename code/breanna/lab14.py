# Pick-6 Lottery

import random


# function to generate six random numbers
def pick6():
    return [random.randint(1,99) for x in range(6)]

# function to get the amount of matches with the winning ticket
def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

winning_ticket = pick6()
print(winning_ticket)


balance = 0
expenses = 0
earnings = 0

# compare 1000000 new tickets to the winning ticket
# get the number of matches
# adjust balance, expenses, and earnings based off of given amounts
for i in range(100000):
    new_ticket = pick6()
    balance -= 2
    expenses += 2
    matches = num_matches(winning_ticket, new_ticket)
    if matches == 6:
        balance += 25000000
        earnings += 25000000
    elif matches == 5:
        balance += 1000000
        earnings += 1000000
    elif matches == 4:
        balance += 50000
        earnings += 50000
    elif matches == 3:
        balance += 100
        earnings += 100
    elif matches == 2:
        balance += 7
        earnings += 7
    elif matches == 1:
        balance += 4
        earnings += 4
    

print("Total expenses: ", expenses)
print("Total earnings: ", earnings)
print("Final balance: ", balance)

