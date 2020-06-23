"""
This program determines whether an input string containing a credit card number is valid
Functions are initiated so I can try to organize code modularly after
I get it run in one function 'validate_credit_card'
"""

# create func that converts the input string into a list of ints
def convert_string_to_ints():
    pass

# '' that slices last digit and stores last digit in variable named 'check_digit'
def get_check_digit():
    pass

# '' that reverses the order of the digits
def reverse_order():
    pass

# '' that doubles every other element in the reversed list
def double_every_other():
    pass

# '' that subtracts nine from numbers over nine
def subtract_9_if_over_9():
    pass

# '' that sums all values in the list
def sum_all_values():
    pass

# '' that stores second digit of sum as 'second_digit'
def second_digit_of_sum():
    pass

# '' that compares 'check_digit' to 'second_digit'
def compare_check_and_second():
    pass

# create func that passes card_num from main in and runs all steps for validation. Print 'Valid' or 'Not Valid'
def validate_credit_card(card_num):

    # string to list of integers
    int_list = list(card_num)
    for i in range(len(int_list)):
        int_list[i] = int(int_list[i])
    print(int_list) # TEST: pass

    # remove last digit and store it as 'check_digit'
    check_digit = int_list.pop(len(int_list)-1)
    print(check_digit) # TEST: pass
    print(int_list) # TEST: pass

    # reverse the order of int_list
    int_list.reverse()
    print(int_list) # TEST: pass

    # double every other value of int_list
    for i in range(len(int_list)):
        if i % 2 == 0:
            int_list[i] *= 2
    print(int_list) # TEST: pass

    # subtract 9 from numbers over 9
    for i in range(len(int_list)):
        if int_list[i] > 9:
            int_list[i] -= 9
    print(int_list) # TEST: pass

    # get the sum of all numbers in list
    sum_int_list = sum(int_list)
    print(sum_int_list) #TEST: pass

    # store second digit of sum, store in a variable 'second_digit'
    
    second_digit = sum_int_list % 10
    print(second_digit) # TEST: pass

    # compare 'second_digit' to 'check_digit'
    if second_digit == check_digit:
        print("Valid :)")
    else:
        print("Faudulent Number!!\nThe authorities are being contacted...")

# run main
if __name__ == "__main__":
    card_num = input("Enter your credit card number: ")
    validate_credit_card(card_num)