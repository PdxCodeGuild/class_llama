
'''
Let's build a program to manage a list of contacts. To start, we'll build a CSV 
('comma separated values') together, and go over how to load that file. Headers might consist 
of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of 
dictionaries, one dictionary for each user. The text in the header represents the keys, 
the text in the other lines represent the values.
'''
with open('advancement.csv' , 'r') as file:
    lines = file.read().split('\n')
    #print(lines)
    
advance_names = []

# creates two list of keys and values
for line in range(len(lines)): 
    key_1 = lines[0]
    key_1 = key_1.split()
    val = lines[line]
    val = val.split()

    valdict = dict(zip(key_1, val)) #combines lists into tuple and then dictionary
    advance_names.append(valdict)
print(advance_names)

def person_lookup(): # looks up and retreives personnel information
    user_1 = input("Who would you like to locate:")
    for person in advance_names:
        if person['lastname'] == user_1:
            print(person)

person_lookup()

# def add_person():
#     new_person = 
#     r = input("What is the sailor's rate:")
#     ln = input("What is the sailor's last name:")
#     fn = input("What is the sailor's first name:")
#     eligible = input("Are they exam eligible:")  #asks for information for creating new entry

