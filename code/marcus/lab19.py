def blackjacklab():
    print("Welcome to the Professional's Table")
    card1 = input("What is your first card?: ")
    if card1 == "J":
        card1 = 10
    elif card1 == "K":
        card1 = 10
    elif card1 == "Q":
        card1 = 10
    elif card1 == "A":
         card1 = 1
    else:
        card1 = int(card1)

    card2 = input("What is your second card?: ")
    if card2 == "J":
        card2 = 10
    elif card2 == "K":
        card2 = 10
    elif card2 == "Q":
        card2 = 10
    elif card2 == "A":
            card2 = 1
    else:
        card2 = int(card2)

    card3 = input("What is your third card?: ")
    if card3 == "J":
        card3 = 10
    elif card3 == "K":
        card3 = 10
    elif card3 == "Q":
        card3 = 10
    elif card3 == "A":
            card3 = 1
    else:
        card3 = int(card3)
    hand = (card1 + card2 +card3)
    if hand == 21:
        print(hand, "Blackjack!")
    elif hand < 16:
        print(hand, "I'd recommend hitting.")
    elif hand > 16:
        print(hand, "You should probably stay, but what do I know. I'm just a string")
    elif hand > 21:
        print(hand, "That's definitely a bust.")

    
blackjacklab()



