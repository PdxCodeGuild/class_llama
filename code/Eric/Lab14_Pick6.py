import random

def winning_nums():
    winners = [random.randint(1,99) for num in range(6)]
    return winners

def lotto_player():
    quick_pick = [random.randint(1,99) for num in range(6)]
    return quick_pick

# matches player quick pick w/ winning lottery numbers
def comp(winner, player):
    winning_matches = 0
    for i in range(len(player)):
        if player[i] == winner[i]:
            matches += 1
    return winning_matches

# displays what the player ends up winning
def prize_moola(num):
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
    for expenses in range(times):
        
        balance -= 2
        winner = winning_nums()
        chance = lotto_player()
        matches = comp(winner, chance)
        balance += prize_moola(matches)
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




   

