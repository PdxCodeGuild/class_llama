# Credit Card Validator

card_num = 4

card_number = input("Enter your 16 digit credit card number: ")

def validate(card_num):

    sum_ = 0
    card_num = card_num[::-1]

    for i in range(len(card_num)):
        if i % 2 == 1:
            double_it = int(card_num[i]*2)
            if len(str(double_it)) == 2:
                sum_ + sum([eval(i) for i in (str(double_it))

    else:
        sum_+= double_it

    if sum_ % 10 == 0:
        response = "Valid Card"

    else:
        response = "Invalid Card"

