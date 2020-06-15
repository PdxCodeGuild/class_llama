# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"

# create card_total dict
card_total = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# define blackjack_advice 
def blackjack_advice(x, y, z):
    sum = card_total[x] + card_total[y] + card_total[z]
    # advise user based on their card total
    if sum < 17:
        advise = f"\n{sum} Hit!\n"
    elif 21 > sum >= 17:
        advise = f"\n{sum} Stay.\n"
    elif sum == 21:
        advise = f"\n{sum} Blackjack!\n"
    else:
        advise = f"\n{sum} Already Busted.\n"
    return advise

# welcome user to blackjack advice program
print("\nWelcome to the Blackjack Advice program! ")

# prompt user for their cards
first_card = input("\nWhat's your first card?: ").upper()
second_card = input("\nWhat's your second card?: ").upper()  
third_card = input("\nWhat's your third card?: ").upper()

# print / call blackjack_advice function / advise user
print(blackjack_advice(first_card, second_card, third_card))










