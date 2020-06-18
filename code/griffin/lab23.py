with open('medieval contacts.csv', 'r') as file:
    lines = file.read().split('\n')

dict_list = []

for line in lines:
    temp_list = line.split(",")
    temp_dict = {}
    for line in temp_list:
        very_temp_list = line.split(":")
        very_temp_list[0] = very_temp_list[0].strip()
        very_temp_list[1] = very_temp_list[1].strip()            
        temp_dict[very_temp_list[0]] = very_temp_list[1]
    dict_list.append(temp_dict)

def create_contact():
    while True:
        medieval_myspace = {}
        name = input("how doth thif one be known by thine companionf? ")
        medieval_myspace["name"] = name
        house = input("to which lord if their allegianfe pledged? ")
        medieval_myspace["house"] = house
        house_words = input("what cry fhalt they utter when charging upon enemief of their house? ")
        medieval_myspace["house words"] = house_words
        status = input("verily, how doth thif knave occupy their time? ")
        medieval_myspace["status"] = status
        dict_list.append(medieval_myspace)
        print(f"thine lift of ne'er-do-wellf if: {dict_list}")
        stop_quest = input("if there another thou wifheft to record? (y/n) ")
        if stop_quest == "n":
            break

def retrieve_contact():
    search = input("which contact do you wifh to view? ")
    for contact in dict_list:
        if contact["name"] == search:
            print(contact)

def main():
    retrieve_contact()
        
    

if __name__ == "__main__":
    main()



    