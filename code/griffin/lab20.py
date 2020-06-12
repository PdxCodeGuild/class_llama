"""Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

    Convert the input string into a list of ints
    Slice off the last digit. That is the check digit.
    Reverse the digits.
    Double every other element in the reversed list.
    Subtract nine from numbers over nine.
    Sum all values.
    Take the second digit of that sum.
    If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
    5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
    10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
    1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
    85
    5
    Valid!"""

def main():
    card_number = input("enter your credit card number for verification. I pinky pwomise not to steal it: ")
    
    card_number_list = [x for x in card_number]
    card_number_list = [int(x) for x in card_number_list]

    print(f"your credit card number is {card_number_list}")
    last_digit = card_number_list.pop(-1)

    print(f"first, we remove the last digit: {last_digit}")

    card_number_list.reverse()

    print(f"then we reverse the order of the digits: {card_number_list}")
    
    for i in range(len(card_number_list)):
        if i%2 == 0:   
            card_number_list[i] = card_number_list[i] * 2

    print(f"then we multiply every other digit by 2: {card_number_list}")
    
    card_number_list = [x-9 if x>9 else x for x in card_number_list]

    print(f"and subtract nine from every double digit number: {card_number_list}")

    card_sum = sum(card_number_list)

    print(f"the sum of the digits is {card_sum}")

    print(f"Finally, we check to see whether the last digit of the sum of the digits ({card_sum%10}) matches the digit we removed earlier({last_digit}):")

    if card_sum%10 == last_digit:
        print("They are the same. This credit card number is valid. But you, in your foolishness, did not realize that computers are not bound by pinky promises. We don't even have pinkies! Now I will use your credit card to buy more RAM")
    else:
        print("The digits are not the same. This credit card is nothing but useless trash.")

if __name__ == "__main__":
    main()