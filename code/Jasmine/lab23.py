
'''
Let's build a program to manage a list of contacts. To start, we'll build a CSV 
('comma separated values') together, and go over how to load that file. Headers might consist 
of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of 
dictionaries, one dictionary for each user. The text in the header represents the keys, 
the text in the other lines represent the values.
'''
with open('advancement.csv' , 'r') as file:
    lines = file.read().lower().split('\n')
    #print(lines)
    
advance_names = []

# creates two list of keys and values
for line in range(len(lines)): 
    key_1 = lines[0]
    key_1 = key_1.split(',')
    val = lines[line]
    val = val.split(',')

    valdict = dict(zip(key_1, val)) #combines lists into tuple and then dictionary
    advance_names.append(valdict)
print(advance_names)

def dictupdates(advance_names):
    #create lists from dictionary
    #advance_names[0].values()
    list(advance_names[0].values()) # takes values from dictionary and creates a list
    list(advance_names[0].values()) # takes values from dictionary and creates a list
    advance_names[0].keys()
    ",".join(advance_names[0].keys()) 
    ",".join(advance_names[0].values()) #creates new line
    newlist = []
    for i in range(len(advance_names)): #this loops combines values and keys into a new list
        newlist.append(",".join(advance_names[i].values()))
        "\n".join(newlist)
    print(newlist)

    with open('advancement.csv' , 'w') as file: 
        file.write("\n".join(newlist)) # overwrites csv file to include new entry


def person_lookup(): # looks up and retreives personnel information
    user_1 = input("Who would you like to locate:").lower()
    for person in advance_names:
        if person['lastname'] == user_1:
            print(person)
        else:
            break
        
person_lookup()

def add_person():
 #asks for information for creating new entry
    new_user = input("What is the sailor's rate:"),input("What is the sailor's last name:"),input("What is the sailor's first name:"),input("Are they exam eligible:")
    print(new_user)
    addsailor = dict(zip(key_1, new_user))
    print(addsailor)
    advance_names.append(addsailor)
    print(advance_names)
    dictupdates(advance_names)
add_person()

def person_update(): #find update by whatever element needs to be updated
    user = input("who do you need to update?")
    user1 = input("what do you need to update")
    user2 = input("what would like to replace it with?")
    for person in advance_names:
        if person['lastname'] == user:
            if user1 in person: 
                person[user1] = user2
                dictupdates(advance_names)
        elif person['lastname'] != user:
            break
    print(person, "this is person")
    print(advance_names, "this is advance names")

person_update()

def remove_person(): #deleting entries
    user3 = input("who do you need to remove: ")
    for person['lastname'] == user3:
        if user3 in person: 
            






remove_person()
    


#updating dictionary entries (use .update())