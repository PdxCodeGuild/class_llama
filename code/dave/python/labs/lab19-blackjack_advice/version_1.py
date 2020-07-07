"""
This program gives basic blackjack advice during a game by asking for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.
"""

# store values for cards in a dictionary
card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'J': 10, 'Q': 10, 'K': 10}



# initailize variables
card_sum = 0

def main():

    ''' prompt user for 3 cards create while loop that asks
        for user card input. if not valid it will keep
        prompting until correct value is input
    '''
    first_card = input("What's your first card? ").upper()
    while first_card not in card_values.keys():
        first_card = input("Not a valid card, enter another card value for first card: ").upper()
    print(first_card)

    second_card = input("What's your second card? ").upper()
    while second_card not in card_values.keys():
        second_card = input("Not a valid card, enter another card value for second card: ").upper()
    print(second_card)

    third_card = input("What's your third card? ").upper()
    while third_card not in card_values.keys():
        third_card = input("Not a valid card, enter another card value for third card: ").upper()
    print(third_card)

    first_card = card_values[first_card]
    second_card = card_values[second_card]
    third_card = card_values[third_card]


    card_sum = first_card + second_card + third_card

    if card_sum < 17:
        print(str(card_sum) + " Hit")
    elif card_sum > 17 and card_sum < 21:
        print(str(card_sum) + " Stay")
    elif card_sum == 21:
        print(str(card_sum) + " Blackjack!!")
    else:
        print(str(card_sum) + " Already Busted")


if __name__ == '__main__':
    main()