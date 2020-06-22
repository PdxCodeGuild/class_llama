# Contact List


with open('contacts.csv', 'r') as file:
    # split twice
    # split each line into a list of strings
    lines = file.read().split('\n')
    # make each line a list
    split_lines = []
    # split at each comma
    for line in lines:
        split_lines.append(line.split(','))
    # print(split_lines)

    # keys are from the first line/list
    keys = split_lines[0]

    contacts = []
    # iterate through all other lines (after key line, 0)
    for k in range(1, len(split_lines)):
        # match keys to each value, new dictionary for each new line
        contacts.append(dict(zip(keys, split_lines[k])))
    print(contacts)


# function to create a new contact and informaton
def create():
    pass

# function to retreive a contact and information
def retreive():
    retreived = input("Choose a contact name to display information: ")
    for contact in contacts:
        # print(contact)
        if contact['Name'] == retreived:
            print(contact)
            # MAKE PRETTY?!
            
retreive()

def retreive_and():
    retreived = input("Choose a contact name to display information: ")
    for contact in contacts:
        # print(contact)
        if contact['Name'] == retreived:
            return(contact)

# function to update a contact and information 
def update():
    retreive_and()
    # update each value one by one?


# function to delete a contact and information
def delete():
    retreive_and()
    # delete contact
    # deleted = ?


# def crud():
#     choice = input("Would you like to create, retreive, update, or delete a contact: ")
#     if choice == "create":
#         create()
#     elif choice == "retreive":
#         retreive()
#     elif choice == "update":
#         update()
#     elif choice == "delete":
#         delete()