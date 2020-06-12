
def main():
    codex = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
    code_numbers = []
    new_code_numbers = []
    new_phrase_list = []
    phrase = input("enter a phrase to send to your spy: ").lower()
    offset = int(input("enter a number with which to encode your message: "))
    
    #goes through the phrase and assigns a numerical value to each letter, then adds it to a list
    for letter in phrase:
        for key in codex:
            if letter == codex[key]:
                code_numbers.append(key)

    #adds 13 to each number in the list, activating the ROT Cipher
    for number in code_numbers:
        new_num = number + offset
        if new_num > 26:
            new_num -= 26
        new_code_numbers.append(new_num)

    #converts the numbers into a list of strings
    for number in new_code_numbers:
        for key in codex:
            if number == key:
                new_phrase_list.append(codex[key])

    new_phrase = "".join(new_phrase_list)


    print(f"your agent will be sent the following: {new_phrase}")





if __name__ == "__main__":
    main()