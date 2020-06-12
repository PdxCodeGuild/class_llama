
from string import ascii_lowercase


def superspystuff():
    in_text = input("Please enter a lowercase string of letters: ")
    letters = []
    # adding letters to the empty letters list
    for x in in_text:
        letters.append(ascii_lowercase.index(x))
    print(letters)
    new_list = []
    # adding rotated numbers to the empty new_list
    num = int(input("How far do you want to shift them (pick a number): "))
    for rot in letters:
        rot += num
        # check if number is over 25, start index back at 0
        if rot > 25:
            rot %= 26
            new_list.append(rot)
        else:
            new_list.append(rot)
    print(new_list)
    new_letters = []
    # getting new letters from the new index numbers from ascii_lowercase
    for letters in new_list:
        new_letters.append(ascii_lowercase[letters])
    # joining list elements together in a string
    out_text = "".join(new_letters)
    print(out_text)
    # return out_text


superspystuff()