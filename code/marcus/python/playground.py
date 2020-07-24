
from string import ascii_lowercase
def num():
    num = int(input("How far do you want to shift them (pick a number): "))
    return num

def superspystuff():
    in_text = input("Please enter a lowercase string of letters: ")
    
    letters = []

    # adding letters to the empty letters list
    for x in in_text:
        if x == " ":
            letters.append(x)
            in_text.replace(x,"")
        else: 
            letters.append(ascii_lowercase.index(x))
    
    # print(letters)

    new_list = []
    num1 = num()
    # num = int(input("How far do you want to shift them (pick a number): "))
    # store = store + num
    # adding rotated numbers to the empty new_list
    for rot in letters:
        if rot == " ":
            pass
        else:
            rot += num1

        # check if number is over 25, start index back at 0 
        if rot == " ":
            new_list.append(rot)
        elif rot > 25:
            rot %= 26
            new_list.append(rot)
        else:
            new_list.append(rot)
    # print(new_list)

    new_letters = []

    # getting new letters from the new index numbers from ascii_lowercase
    for letters in new_list:
        if letters == " ":
            new_letters.append(letters)
        else:
            new_letters.append(ascii_lowercase[letters])

    # joining list elements together in a string
    out_text = "".join(new_letters)

    print(out_text,num1)
    decode(out_text,num1)
    # print(store)
    return out_text, num1

def decode(out_text, num1):
    num2 = num1
    letters = []
    new_list = []
    
    for x in out_text:
        if x == " ":
            letters.append(x)
            out_text.replace(x,"")
        else: 
            letters.append(ascii_lowercase.index(x))
    # print(letters)
    reverse = 0
    for rot in letters:
        if rot == " ":
            pass
        else:
            rot -= num2

        # check if number is over 25, start index back at 0 
        if rot == " ":
            new_list.append(rot)
        elif rot < 0:
            remder = rot % 26
            reverse = (reverse * 26) + remder
            new_list.append(reverse)
            reverse = 0
        else:
            new_list.append(rot)
    # print(new_list)
    new_letters = []

    # getting new letters from the new index numbers from ascii_lowercase
    for letters in new_list:
        if letters == " ":
            new_letters.append(letters)
        else:
            new_letters.append(ascii_lowercase[letters])
    
    # joining list elements together in a string
    decoded = "".join(new_letters)
    # print(decoded, 'this is line 98')
    return decoded


superspystuff()
