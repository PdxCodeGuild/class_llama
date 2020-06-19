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

def create_contact(contact_list):
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
        contact_list.append(medieval_myspace)
        print(f"thine lift of ne'er-do-wellf if: {contact_list}")
        stop_quest = input("if there another thou wifheft to record? (y/n) ")
        if stop_quest == "n":
            break
    return contact_list

def retrieve_contact(contact_list):
    search = input("which contact do you wifh to view? ")
    for contact in contact_list:
        if contact["name"] == search:
            print(contact)
            return contact

def update_contact(contact_list):
    contact = retrieve_contact(contact_list)
    attribute = input("Would you like to change name, house allegiance, house words, or status? ")
    change  = input("What would you like to change it to? ")
    for d in contact_list:
        if d == contact:
            d[attribute] = change
    return contact_list
    

def delete_contact(contact_list):
    contact = retrieve_contact(contact_list)
    contact_list.remove(contact)
    print(f"{contact} has been removed")
    return contact_list

def save_changes(contacts):
    contacts_string = ""
    for contact in contacts:
        for key in contact:
            contacts_string = contacts_string + key + ": " + contact[key]
            if key != "status":
                contacts_string = contacts_string + ", "
        contacts_string = contacts_string + "\n"
    print(contacts_string)        
    """with open("medieval contacts.csv", "w") as contact_list:
        contact_list.write(contact_string)"""

def main():
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
    while True:
        choice = int(input("""What would you like to do?
        (1) Create new contact 
        (2) Search your contacts 
        (3) Update a contact 
        (4) Delete a contact
        (5) Show all contacts
        (6) Save changes
        (7) Quit
        """))    
        if choice == 1:
            create_contact(dict_list)
        elif choice == 2:
            retrieve_contact(dict_list)
        elif choice == 3:
            update_contact(dict_list)
        elif choice == 4:
            delete_contact(dict_list)    
        elif choice == 5:
            print(dict_list)
        elif choice == 6:
            save_changes(dict_list)
        elif choice == 7:
            break

    

if __name__ == "__main__":
    main()



    