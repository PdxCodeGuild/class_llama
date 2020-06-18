"""
# Lab 15: Number to Phrase

Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 100-999.

Hint: you can use modulus to extract the ones and tens digit.

```python
x = 67
tens_digit = x//10
ones_digit = x%10
```
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.
"""

# initialize a dictionary for num_to_words
ones_digit = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
              5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',}
teen_digit = {0: 'Ten', 1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen',
              5: 'Fifteen', 6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen',
              9: 'Nineteen'}
tens_digit = {0: '', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
              6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
hund_digit = {0: '', 1: 'One-Hundred', 2: 'Two-Hundred', 3: 'Three-Hundred',
              4: 'Four-Hundred', 5: 'Five-Hundred', 6: 'Six-Hundred',
              7: 'Seven-Hundred', 8: 'Eight-Hundred', 9: 'Nine-Hundred'}


# create num_to_phrase function
def num_to_phrase(num):

    # isolate the tens
    hund = int(num)//100
    tens = int(num)//10
    ones = int(num)%10

    # if statements to determine ones, teens, and tens digits
    if tens == 0:
        return ones_digit[int(num)]
    elif tens == 1:
        return teen_digit[int(ones)]
    elif tens >= 1:
        return tens_digit[int(tens)] + "-" + ones_digit[int(ones)]
    elif hund >= 1:
        return hund_digit[int(hund)] + "and " + tens_digit[int(tens)] + "-" + ones_digit[int(ones)]
    else:
        print("You did not enter a number in the range 0-99")


# main function
def main():

    # take input from the user
    num_input = input("Enter a number between 0-99: ")

    # print the results of num_to_phrase func
    print(num_to_phrase(num_input))

main()