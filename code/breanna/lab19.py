# Blackjack Advice


def blackjack():

    f_card = input("What is your first card? ")

    if f_card == "J":
        f_card = 10
    elif f_card == "Q":
        f_card = 10
    elif f_card == "K":
        f_card = 10
    elif f_card == "A":
        f_card = 1
    else:
        f_card = int(f_card)

    s_card = input("What is your second card? ")

    if s_card == "J":
        s_card = 10
    elif s_card == "Q":
        s_card = 10
    elif s_card == "K":
        s_card = 10
    elif s_card == "A":
        s_card = 1
    else:
        s_card = int(s_card)

    t_card = input("What is your third card? ")

    if t_card == "J":
        t_card = 10
    elif t_card == "Q":
        t_card = 10
    elif t_card == "K":
        t_card = 10
    elif t_card == "A":
        t_card = 1
    else:
        t_card = int(t_card)

    total = int(f_card) + int(s_card) + int(t_card)

    if total == 21:
        print(f"{total}, Blackjack!")
    elif total > 21:
        print(f"{total}, bust.")
    elif total < 21 and total >= 17:
        print(f"{total}, stay.")
    elif total < 17:
        print(f"{total}, hit.")


blackjack()