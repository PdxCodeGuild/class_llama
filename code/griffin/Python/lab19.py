import random as r

def main():
    cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"J":10,"Q":10,"K":10}
    total_value = 0


    

    #draws 3 cards
    for n in range(3):
        drawn_card = r.choice(list(cards.keys()))
        total_value += cards[drawn_card]
        print(drawn_card)
    
    print(f"total points: {total_value}")

    #gives very sophisticated advice
    if total_value < 17:
        print("I advise: hit!")
    elif 17 < total_value < 21:
        print("I advise: stay!")
    elif total_value == 21:
        print("Blackjack!")
    else:
        print("ya busted")


if __name__ == "__main__":
    main()
