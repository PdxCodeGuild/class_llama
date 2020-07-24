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

def play_lottery(times):
    expenses = (2 * int(times))
    balance = 0
    for x in range(times):
        
        balance -= 2
        winner = pick6_winners()
        chance = pick6_player()
        matches = compared(winner, chance)
        balance += winnings(matches)
    final_balance = expenses + balance
    roi = final_balance/expenses
        
    if final_balance == 0:
        print("You won nothing!")
    elif final_balance == expenses:
        print(f"You broke even.")
    elif final_balance < expenses: 
        print(f"You spent ${expenses} in all, winning only ${final_balance} in the process.")
        print(f"You lost ${expenses - final_balance} altogether!")
        print(f"That's a success rate of {roi}%!")
    elif final_balance > expenses:
        print(f"You won ${balance}!")
        print(f"You spent ${expenses} in all, winning ${final_balance} in the process.")
        print(f"That's a success rate of {roi}%!")



play_lottery(int(input("How many times do you want to play? ")))




