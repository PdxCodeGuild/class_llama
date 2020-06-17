''' 
Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

1 Convert the input string into a list of ints
2 Slice off the last digit. That is the check digit.
3 Reverse the digits.
4 Double every other element in the reversed list.
5 Subtract nine from numbers over nine.
6 Sum all values.
7 Take the second digit of that sum.
8 If that matches the check digit, the whole card number is valid.

16 digits in cc number

''' 
# take string of numbers and make into a list of integers
# this will convert a # string into integer list
#a_string = "2 4 3 5 3 3 4"
#a_list = a_string.split()
#map_object = map(int, a_list)

#list_of_integers = list(map_object)
#print(list_of_integers)

#16 digits 
user_1 = input("Enter your 16-digit number:")

#converts supplied card number into integer list
a_string = (user_1)
num_list = a_string.split()
map_object = map(int, num_list)

card_num = list(map_object)
check_digit = card_num.pop() # take off last integer
print(card_num)
print(check_digit)

#reverse number 
card_num.reverse()
print(card_num)

# double every other digit by two
card_num = [card_num[i]*(2**(i%2)) for i in range(len(card_num))]
print(card_num)

# subtract 9 from integers over 9, leave single digits as be
card_num = [i - 9 if i > 9 else i for i in card_num]
print(card_num)

# sum of the the number value
sum_of = sum(card_num)
print(sum_of)

#if the second sum matches that check digit (first digit you took off) than the
#number is valid
#is_valid = [card_num]
#valid_card = [card_num ]

#def card_validation(card_num): 

    














#card_validation()