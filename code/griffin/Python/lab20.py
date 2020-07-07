def main():
    card_number = input("enter your credit card number for verification. I pinky pwomise not to steal it: ")
    
    card_number_list = [x for x in card_number]
    card_number_list = [int(x) for x in card_number_list]
    print(f"your credit card number is {card_number_list}")

    last_digit = card_number_list.pop(-1)
    print(f"first, we remove the last digit: {last_digit}")

    card_number_list.reverse()
    print(f"then we reverse the order of the digits: {card_number_list}")
    
    for i, v in enumerate(card_number_list):
        if i%2 == 0:
            card_number_list[i] = card_number_list[i] *2                                                  
    print(f"then we multiply every other digit by 2: {card_number_list}")
    
    card_number_list = [x-9 if x>9 else x for x in card_number_list]
    print(f"and subtract nine from every double digit number: {card_number_list}")

    card_sum = sum(card_number_list)
    print(f"the sum of the digits is {card_sum}")

    print(f"Finally, we check to see whether the last digit of the sum of the digits ({card_sum%10}) matches the digit we removed earlier({last_digit}):")
    if card_sum%10 == last_digit:
        print("They are the same. This credit card number is valid. But you, in your foolishness, did not realize that computers are not bound by pinky promises. We don't even have pinkies! Now I will use your credit card to buy more RAM")
    else:
        print("The digits are not the same. This credit card is nothing but a worthless piece of plastic")

if __name__ == "__main__":
    main()