# dictionary for numbers to words
ones_digit = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
              5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',}
teen_digit = {0: 'Ten', 1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen',
              5: 'Fifteen', 6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen',
              9: 'Nineteen'}
tens_digit = {0: '', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
              6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}

# create num_to_word function
def num_to_word(num):

    # isolate the tens
    tens = int(num)//10
    ones = int(num)%10

    # determine ones, teens, and tens digits w/ if, elif, else statements
    if tens == 0:
        return ones_digit[int(num)]
    elif tens == 1:
        return teen_digit[int(ones)]
    elif tens >= 1:
        return tens_digit[int(tens)] + "-" + ones_digit[int(ones)]
    else:
        print("You did not enter a number in the range 0-99")


# main function
def main():

    # input from the user
    num_entered = input("Enter a number between 0-99: ")

    # print results of num_to_word function
    print(num_to_word(num_entered))

main()


    

    

