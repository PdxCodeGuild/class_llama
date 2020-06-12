# Lab 14, Lottery

import random

# Determines the winning numbers
def pick6_winners():
    win = [random.randint(1, 99) for num in range(6)]
    return win

# How much spent/won
def balancer(times_run, winnings):
    balance = 0
    for x in times:
        balance -= 2
    if winnings > 0:
        balance += int(winnings)
    return balance
    

# Player chooses random 6
def pick6_player():
    ticket = [random.randint(1, 99) for num in range(6)]
    return ticket


# Compares indices
def matches(winners, players):
    matches = 0
    for players[i] in winners[i]:
        matches += 1
    return matches

# Returns prize from winning numbers
def winnings(num):
    if num == 0:
        return "nothing :("
    elif num == 1:
        return "$4"
    elif num == 2:
        return "$7"
    elif num == 3:
        return "$100"
    elif num == 4:
        return "$50,000"
    elif num == 5:
        return "$1,000,000"
    elif num == 6:
        return "$25,000,000"


def play_lottery():
    for x in range(100000):
        pick6_winners()
        pick6_player()




play_lottery()



