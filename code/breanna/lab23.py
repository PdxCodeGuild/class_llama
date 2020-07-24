# Contact List


with open('contacts.csv', 'r') as file:
    # split each line into a list of strings
    lines = file.read().split('\n')
    
    # make each line a list
    split_lines = []
    
    # split at each comma
    for line in lines:
        split_lines.append(line.split(','))

    # keys are from the first line/list
    keys = split_lines[0]

    contacts = []
    
    # iterate through all other lines (1, to the end)
    for k in range(1, len(split_lines)):
        # match keys to each value, new dictionary for each new line
        contacts.append(dict(zip(keys, split_lines[k])))
    
    print(contacts)


def update_file():
    # join keys in list separated by commas
    x = [','.join(keys)]
    
    # loop through contacts, get value of values (put individual dictionaries back into list)
    for value in contacts:
        y = ','.join(value.values())
        # join lists
        x.append(y)
    
    # add new lines after each comma to format for csv
    z = '\n'.join(x)
    
    # write to file
    with open('contacts.csv', 'w') as file:
        file.write(z)


# function to create a new contact and informaton
def create():
    # use index 0 line for keys, split line to get individual keys
    keys = lines[0]
    keys = keys.split(',')
    new_contact = input("Enter the contact's first name: "), input("Enter their favorite animal: "), input("Enter their favorite color: "), input("Enter their favorite fruit: ")
    # convert to dictionary, append to existing contacts list or dictionaries
    new_contact = dict(zip(keys, new_contact))
    contacts.append(new_contact)
    
    print(contacts)

    update_file()


# function to retreive a contact and information
def retreive():
    retreived = input("Choose a contact name to display information: ")
    for contact in contacts:
        if contact['Name'] == retreived:
            print(contact)
            # this could be printed prettier


# function to retreive a contact and information and use in other functions
def retreive_and():
    retreived = input("Choose a contact name to display information: ")
    for contact in contacts:
        if contact['Name'] == retreived:
            return contact


# function to update a contact and information 
def update():
    contact = retreive_and()
    
    update = input("Would you like to update this contact (Y/N): ")
    
    if update == "Y":
        contact['Name'] = input("Enter the contact's first name: ")
        contact['Favorite animal'] = input("Enter their favorite animal: ")
        contact['Favorite color'] = input("Enter their favorite color: ")
        contact['Favorite fruit'] = input("Enter their favorite fruit: ")
        print(f"This contact and information has been updated.\n{contact}")
    elif update == "N":
        pass
    
    update_file()


# function to delete a contact and information
def delete():
    contact = retreive_and()

    delete = input("Would you like you delete this contact and information (Y/N): ")
    
    if delete == "Y": 
        contacts.remove(contact)
        print(f"This contact and information has been deleted.\n{contacts}")
   
        update_file()
   
    elif delete == "N":
        pass


def crud():
    while True:
        choice = input("Would you like to create, retreive, update, or delete a contact (c/r/u/d): ")
        if choice == "c":
            create()
        elif choice == "r":
            retreive()
        elif choice == "u":
            update()
        elif choice == "d":
            delete()

crud()
