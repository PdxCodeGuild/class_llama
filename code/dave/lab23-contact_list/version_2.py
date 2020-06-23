"""
This program manages a list of contacts utilizing a CSV(comma seperated value) file 
and CRUD (Create, Retrieve, Update, Delete).
"""


# create func that opens csv 'file_path' and creates list of dictionaries
def file_to_list(file_path):
    # open and read contacts.csv file
    with open(file_path, 'r') as f:
        lines = f.read().split('\n')
        # print(lines) #works

        people = []

        for i in range(len(lines)):
            dict_keys = lines[0]
            # print(dict_keys) #works
            dict_keys = dict_keys.split(',')
            # print(dict_keys)

            dict_values = lines[i] # slice off headers at index 0, start at index 1
            # print(dict_values) #works
            dict_values = dict_values.split(',')
            # print(dict_values) # works

            dict_items = dict(zip(dict_keys, dict_values))
            # print(dict_items) #works

            people.append(dict_items)
        # print(people) # works
        # print(people[1]['status']) # how to retrieve
        return people


# create func that creates a record
def create_contact(contact_list):
    pass

# create func that retrieves a record
def retrieve_contact(contact_list):

    # ask user for contact to retrieve
    name = input("Enter the name of contact you wish to retrieve: ").lower()
    
    # for loop that searches through name value in contact_list
    for contact in contact_list:
        if name == contact['name']:
            print()
            print(contact['name'], ":", contact['profession'], "--", contact['status'])
            break
    else:
        print("Contact not found. Try again. ")
        

# create func that updates a record
def update_contact(contact_list):
    pass

    # user_input = 

# create func that deletes a record
def delete_contact(contact_list):
    pass


# create main func that runs main if file called directly
if __name__ == "__main__":

    # create variable for file_path so it is more dynamic. Able to use easier in future code.
    file_path = "./contacts.csv"
    contact_list = file_to_list(file_path)

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
                create_contact(contact_list)
            elif choice == 'r':
                print("\nYou chose retrieve.\n")
                choice = 'retrieve'
                retrieve_contact(contact_list)
            elif choice == 'u':
                print("\nYou chose update.\n")
                choice = 'update'
                update_contact(contact_list)
            elif choice == 'd':
                print("\nYou chose delete.\n")
                choice = 'delete'
                delete_contact(contact_list)
            elif choice == 'e':
                print("You chose to exit.\nGoodbye.\n")
                choice = 'exit'
                break
            else:
                input("\nWHOOPS, WRONG INPUT. Try Again (Press Enter To Continue)")
        except ValueError:
            print("\nSorry, try one of the options again. ")
    print("\nTEST Complete you selected to", choice)

