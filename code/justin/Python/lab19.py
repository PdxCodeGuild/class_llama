# Lab 19
# Blackjack

def convert(card):
    # Is it a valid integer?
    if card.isdigit():
        if 10 >= int(card) >= 2:
            return int(card)
        else: 
            return False
    
    # ...or is it a valid face card?
    elif card in ["A", "a"]:
        return 1
    elif card in ["J", "Q", "K", "j", "q", "k"]:
        return 10
    else:
        return False

def main():
    # Card 1
    stop1 = 0
    while stop1 == 0:
        card1 = input("First card: ")
        if convert(card1) is False:
            print("Invalid input.")
            break          
        else:
            stop1 += 1

    #Card 2
    stop2 = 0        
    while stop2 == 0:
        card2 = input("Second card: ")
        if convert(card2) is False:
            print("Invalid input.")
            break
        else: 
            stop2 += 1
    
    # Card 3
    stop3 = 0
    while stop3 == 0:
        card3 = input("Third card: ")
        if convert(card3) is False:
            print("Invalid input.")
            break
        else: 
            stop3 += 1        

    # Adding values
    total = convert(card1) + convert(card2) + convert(card3)
    
    # Results
    if 21 > total >= 17:
        print(f"You're at {total}, you should stay.")
    elif total == 21:
        print("You're at 21, Blackjack!")
    elif total < 17:
        print(f"You're at {total}, maybe you should hit.")
    elif total > 21: 
        print(f"{total}, ya busted :(")

main()
