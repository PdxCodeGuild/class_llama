# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

# Steps
# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance

import random
# randint is pulling for ints between 2 args to fill the 6 nums required for the lotto ticket
winning_nums = [random.randint(1,99) for x in range(6)]

user_ticket = [random.randint(1,99) for x in range(6)]
# compares and prints what numbers are the same/position
comparty = set(winning_nums).intersection(user_ticket)
check = zip(winning_nums,user_ticket)
check2 = list(check)
# checkcheck pulls 
checkcheck = set(winning_nums) & set(user_ticket)
# print(comparty)
# print(checkcheck)
# print(check2)
# count = 0
# for x in checkcheck:
#     comp
#     count =+ 1
#     if count == 100000:

for i in range(100000):
    user_ticket = [random.randint(1,99) for x in range(6)]
    
    print(checkcheck)
        
        
