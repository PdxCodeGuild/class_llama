'''
blackjack

'''

'''
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

'''

import random

#dictonary of cards and their values
card_value = {"2": 2 , "3": 3 , "4": 4 , "5": 5 , 
"6": 6 , "7": 7 , "8": 8 , "9": 9 , "10": 10 , "J": 10 , 
"Q": 10 , "K": 10 , "A": 1} 

#face cards 

cards = ["2" , "3" , "4" , "5" , "6" , "7" , "8" , 
"9" , "10" , "J" , "Q" , "K" , "A"]  

#n is variable for selected cards
def generate_cards(cards):
    print("These are your cards:")
    fc = random.choice(cards)
    sc = random.choice(cards)
    tc = random.choice(cards)
    print(fc, sc, tc)

    #cards and cards worth 
    card_1 = card_value[fc]
    #print(card_1, "card 1 value")
    card_2 = card_value[sc]
    #print(card_2, "card 2 value")
    card_3 = card_value[tc]
    #print(card_3, "card 3 value")

    #add card points together to make point sums 
    card_sum = (card_1 + card_2 + card_3)
    print("Your score:", card_sum)

    #with the point sum, if less than 17, ask them if they want to hit again, 
    #if over 17, tell them to stay
    #if at 21 black jack, you win
    #if over 21, bust 

    if card_sum <= 17: 
        print("Hit again")

    elif card_sum > 17 <20: 
        print("Stay")
    
    elif card_sum == 21: 
        print("BLACKJACK!")

    else:
        print("Bust")

generate_cards(cards)






