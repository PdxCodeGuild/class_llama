with open('lab23csv.csv', 'r') as file:
    lines = file.read().split('\n')


phonebook = []

for line in range(len(lines)):
    # pulls out line 0 which holds what I want for my keys
    keytool = lines[0]
    # creates the individual keys that other entries will pull from
    keytool = keytool.split(',')
    
    # pulls out the other lines that will be used as values
    val = lines[line]
    # splits the lines up into their individual values
    val = val.split(',')
    # combines the keys and values for the csv
    valuedict = dict(zip(keytool, val))
    # addes them back in the dictionary in the form of keys/values
    phonebook.append(valuedict)

# don't ask me how this function works. I can kind of explain it but for the most 
# part, it's magic. It basically destroys the key/value dict and puts it back into 
# how it was retreived from the csv.
def updatefile(phonebook):
    # create some lists from dictionary
    phonebook[0].value()
    list(phonebook[0].values())
    list(phonebook[0].values())
    phonebook[0].keys()
    ','.join(phonebook[0].keys())
    ','.join(phonebook[0].values())

    uploadlist = []
    for i in range(len(phonebook)):
        uploadlist.append(','.join(phonebook[i].values()))
        '\n'.join(uploadlist)
    

    with open('lab23csv.csv', 'r') as file
        file.write('\n'.join(uploadlist)




# function that can pick a user out of the csv and display all of their information
def picknpull():
    # input asking for which user's info to be pulled 
    sherlockuser = input('Who are you looking for?: ')
    for person in phonebook:
        if person['name'] == sherlockuser:
            print(person)
# always define a new function for each step in CRUD
# remember keys are stored in keytool
# don't overthink how to put keys and values together


# function to add someone to the csv
def newentry():
    sherlocknew = input('Who would you like to add?: '),input('What is their favorite show?: '),input('What is their favorite sport?: ')
    # makes it nice and neat so Python will allow it to be appended to the csv
    sherlockadded = dict(zip(keytool,sherlocknew))
    # adding it to the dict controlled by the csv
    phonebook.append(sherlockadded)


# function to delete a contact
def getouttahere():
    # has the user pick a person using the old function
    contact = picknpull()
    # this input confirms whether the user would like to delete entry
    delete = input("Would you like you delete this contact and information (Y/N): ")
    if delete == "Y": 
        # removes the contact
        phonebook.remove(contact)
        print("This contact and information has been deleted.")
    elif delete == "N":
        pass


def changeuser():
    # lets the user choose who to update
    updated = picknpull()
    # chooses what they'll update
    updater = input('what would you like to update?: ')
    # updates the show
    if updater == 'favorite show':
        updatershow = input('Please enter the new information: ')
        updated.append(updatershow)
    # updates the sport
    if updater == 'favorite sport':
        updatersport = input('Please enter the new information: ')
        updated.append(updatersport)
    else:
        pass
    print(phonebook)







    