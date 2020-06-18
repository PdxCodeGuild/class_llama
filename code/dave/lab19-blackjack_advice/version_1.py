"""
This program gives basic blackjack advice during a game by asking for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.
"""

# store values for cards in a dictionary
card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'J': 10, 'Q': 10, 'K': 10}



# initailize variables
card_sum = 0

def correct_value(val):

    # check if value entered matches any key in card_values
    while val != card_values.keys():
        print(input("Not a valid card, enter another card value: "))
    return val


def main():

    # prompt user for 3 cards

    first_card = input("What's your first card? ").upper()
    print(first_card)


if __name__ == '__main__':
    main()