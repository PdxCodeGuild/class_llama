"""
This program manages a list of contacts utilizing a CSV(comma seperated value) file 
and CRUD (Create, Retrieve, Update, Delete).
"""
import csv

# create func that saves updated to csv file
def save_list(people, file_path):
    print(people)
    empty_list = []

    people[0].values() #TEST: add print()

    list(people[0].values())
    list(people[0].values())

    people[0].keys()
    ','.join(people[0].keys())
    ','.join(people[0].values())

    # create for loop to reverse operations in file_to_list 
    for i in range(len(people)):
        
        empty_list.append(','.join(people[i].values()))
        '\n'.join(empty_list)
    with open(file_path, 'w') as f:
        f.write('\n'.join(empty_list))

# create func that creates a record
def create_contact(contact_list, file_path):

    # get user input for name, status, and profession for contact
    name = input("What is your new contacts name: ").lower()
    status = input("What is your new contacts status: ").lower()
    profession = input("What is your new contacts profession: ").lower()

    # append new user name, status, and profession to create_contact list
    contact_list.append({'name':name, 'status':status, 'profession':profession})
    print(contact_list)

    save_list(contact_list, file_path)
    # return new_contact
    return contact_list


# create func that retrieves a record
def retrieve_contact(people):

    # ask user for contact to retrieve
    name = input("Enter the name of person you wish to retrieve: ").lower()
    
    # for loop that searches through name value in contact_list
    for i in people:
        if name == i['name']:
            print()
            print(i['name'], ":", i['profession'], "--", i['status'])
            return i
    else:
        print("Person not found. Try again. ")
        

# create func that updates a record
def update_contact(people, file_path):
    who = input("Who would you like to update? ")
    what = input("What would you like to change? (name, status, profession) ")
    change = input(f"What would you like to change {what} to: ")

    for i in people:
        if i['name'] == who:
            if what in i:
                i[what] = change
                save_list(people, file_path)


# create func that deletes a record
def delete_contact(people, file_path):
        person = retrieve_contact(people)
        confirm = input(f"Are you certain you want to delete {person} permanently? (yes/no) ").lower()
        for i in people:
            if i['name'] == person['name'] and confirm == 'yes':
                # del people[people.index(i)]
                people.remove(i)
                save_list(people, file_path)

# create main func that runs main if file called directly
if __name__ == "__main__":

    # create variable for file_path so it is more dynamic. Able to use easier in future code.
    file_path = "./contacts_copy.csv"
    # contact_list = file_to_list(file_path)

    with open(file_path, 'r') as f:
        lines = f.read().split('\n')
        print(lines) #TEST: pass

        people = []

        for i in range(len(lines)):
            dict_keys = lines[0]
            print(dict_keys) #TEST: pass
            dict_keys = dict_keys.split(',')
            print(dict_keys)

            dict_values = lines[i] # slice off headers at index 0, start at index 1
            print(dict_values) #TEST: pass
            dict_values = dict_values.split(',')
            print(dict_values) #TEST: pass

            dict_items = dict(zip(dict_keys, dict_values))
            print(dict_items) #TEST: pass

            people.append(dict_items)
        print(people)
        save_list(people, file_path)
    # while loop that runs until user exits
    while True:    
        try:

            # print option menu for user to select from
            print("""
____________________________________ 
------------------------------------
What do you want to do?             
Enter the letter in parenthesis: 

(C) create new contact                
(R) retrieve contact info             
(U) update contact info               
(D) delete contact info               
(E) exit                              
____________________________________
------------------------------------
            """)
            
            # store user's 'choice' in a variable 
            choice = input("What would you like to do? : ").lower()
            print()

            # if statement that determines if user entered a valid option from menu
            # option menu keeps looping unless user enters 'e' then while loop breaks.
            if choice == 'c':
                print("\nYou chose create.\n")
                choice = 'create'
                create_contact(people, file_path)
            elif choice == 'r':
                print("\nYou chose retrieve.\n")
                choice = 'retrieve'
                retrieve_contact(people)
            elif choice == 'u':
                print("\nYou chose update.\n")
                choice = 'update'
                update_contact(people, file_path)
            elif choice == 'd':
                print("\nYou chose delete.\n")
                choice = 'delete'
                delete_contact(people, file_path)
            elif choice == 'e':
                print("You chose to exit.\nGoodbye.\n")
                choice = 'exit'
                break
            else:
                input("\nWHOOPS, WRONG INPUT. Try Again (Press Enter To Continue)")
        except ValueError:
            print("\nSorry, try one of the options again. ")
    print("\nTEST Complete you selected to", choice)

