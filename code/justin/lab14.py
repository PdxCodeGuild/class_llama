# Lab 14, Lottery

import random

# Ticket number functions
def pick6_winners():
    win = [random.randint(1, 99) for num in range(6)]
    return win

def pick6_player():
    ticket = [random.randint(1, 99) for num in range(6)]
    return ticket

# Compares tickets
def compared(winner, player):
    matches = 0
    for i in range(len(player)):
        if player[i] == winner[i]:
            matches += 1
    return matches

# Returns prize from winning numbers
def winnings(num):
    if num == 0:
        return 0
    elif num == 1:
        return 4
    elif num == 2:
        return 7
    elif num == 3:
        return 100
    elif num == 4:
        return 50000
    elif num == 5:
        return 1000000
    elif num == 6:
        return 25000000

def play_lottery():
    balance = 0
    for x in range(100000):
        
        balance -= 2
        winner = pick6_winners()
        chance = pick6_player()
        matches = compared(winner, chance)
        balance += winnings(matches)


    print(f"Your final balance is ${balance}")

    '''
    if balance >= 0:
        final_balance = balance + 200000
        print(f"You broke even at least, impressive! You won {final_balance} altogether")
    elif balance < 0 and balance > -200000:
        print(f"Your  You won {final_balance} altogether")
    '''


play_lottery()



