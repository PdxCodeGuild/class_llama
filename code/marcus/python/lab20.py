import random

card = [random.randint(1,10) for x in range(16)]
cardi = list(card)
print(cardi)

make_sure_its_correctier = cardi[15]
print(make_sure_its_correctier)
 

cardi.pop(15)
print(cardi)


cardi.reverse()
print(cardi)


cardi[0::2] = [x*2 for x in card[0::2]]
print(cardi)


cardi = [x-9 if x > 9 else x for x in card]
print(cardi)


cardtotes = sum(cardi)
print(cardtotes)


cardification = str(cardtotes)
cardboi = cardification[1]

print(cardboi)


if int(cardboi) == int(make_sure_its_correctier):
    print("Valid!")
else:
    print("Not valid.")