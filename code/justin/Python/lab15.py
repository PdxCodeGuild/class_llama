# Version 1

def wordizer(converted):
    num = int(converted)
    # Dictionaries
    double_digits = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }
    single_digits = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    outliers = {
        0: 'Zero',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
            }
   
    if num in outliers:
        return (outliers[num])
    
    elif num in range(1,10):
        return single_digits[num]

    else:
        tens = num // 10
        ones = num % 10

        if tens in range(2,9) and ones == 0:
            return double_digits[tens]
        else:
            return (double_digits[tens] + "-" + single_digits[ones])

# Main function to input an integer number.
def main():
    while True:
        user = input("Type a number between 0-99: ")
        if user.isdigit() is False:
            print("Invalid entry.")
        elif int(user) in range(0, 100):
            print(wordizer(user))
        else: 
            print("Invalid entry.")

main()