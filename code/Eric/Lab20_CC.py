# Credit Card Validation Program

import random

cred_card = [random.randint(1,10) for x in range(16)]
card = list(cred_card)
print(card)


verify_cc = card[15]
print(verify_cc)	
 
# .pop() removes and returns last object or obj from the list
card.pop(15)
print(card)

# reverses objects of list in place
card.reverse()
print(card)

# Double the digits
card[0::2] = [x*2 for x in card[0::2]]
print(card)


card = [x-9 if x > 9 else x for x in card]
print(card)


cc_digits = sum(card)
print(cc_digits)


card_verif = str(cc_digits)
card_x = card_verif[1]

print(card_x)


if int(card_x) == int(verify_cc):
    print("Valid Credit Card")
else:
    print("NOT Valid")





















