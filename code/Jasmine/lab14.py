import random

#pick 6 rand numbers
def pick6():
    return[random.randint(1,99) for x in range(6)]
print(pick6())

def num_match(winning, tickets):
    matches = 0 

    for win, tix in zip(winning, ticket):
        if == win, tix: 
             matches += 1
    return matches

#define variables
balance = 0
earnings = 0
expenses = 0

    for n range(100000):
        currenttick = pick(6)
        balance -= 2
        expenses += 2
        matches = num_match(winning_ticket, currrenttick)
        
        if matches = 6:
            balance += 2500000
            expensees += 2500000
        elif matches = 5: 
            balance += 100000
            expenses += 100000
        elif matches = 4: 
            balance += 50000
            expenses += 50000
        elif matches = 3:
            balance += 100
            expenses += 100
        elif matches = 2: 
            balance += 7
            expenses += 7
        elif matches = 1: 
            balance += 4
            expenses += 4

print("Balance:" , balance)
print("Expenses:" , expenses)
print("ROI:" , (earnings - expenses/)/ expenses)

        
        